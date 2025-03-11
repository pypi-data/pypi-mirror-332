"""
Module that implements learning workflow for model generation

@author fabiano.tavares
"""
import json
import pickle
import shutil
from datetime import datetime, date, time, timedelta
from typing import Dict, Optional

import numpy as np
import pandas as pd
from datasets import Dataset
from loguru import logger
from pynvml import *
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, \
    EarlyStoppingCallback, AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
from transformers import DataCollatorWithPadding
from transformers.pipelines.base import KeyDataset

from .preprocessor import Preprocessor
from .utils.parse import final_model_name

# config pandas warning: A value is trying to be set on a copy of a slice from a DataFrame.
pd.options.mode.chained_assignment = None  # default='warn'
DATE_FORMAT = '%d/%m/%Y'


class LLMTrainer:
    def __init__(self, model_name_or_path, text_column, label_column, label2id: dict = None, id2label: dict = None,
                 max_seq_length=512, training_args: TrainingArguments = None):

        self.model_name_or_path = model_name_or_path
        self.id2label = id2label
        self.label2id = label2id
        self.text_column = text_column
        self.label_column = label_column
        self.training_args = training_args
        self.max_length = max_seq_length
        self.tokenizer: Optional[BertTokenizer] = None
        self.model: Optional[BertForSequenceClassification] = None
        self.data_collator: Optional[DataCollatorWithPadding] = None
        self.trainer: Optional[Trainer] = None
        self.load_model(model_name_or_path)

    def freeze(self, freeze=True, num_min_freeze=2):
        if freeze:
            total_layers = len(
                set([int(name.split(".")[3]) for name, param in self.model.named_parameters() if 'layer' in name]))
            for name, param in self.model.named_parameters():
                if 'layer' in name:
                    try:
                        layer_index = int(name.split(".")[3])
                        if layer_index <= total_layers - num_min_freeze:
                            param.requires_grad = False
                    except:
                        continue

    def tokenize_preprocess(self, dataset_df: pd.DataFrame, lbl2id: dict):
        __df = dataset_df.reset_index(drop=True)
        __df.rename(columns={self.label_column: 'labels'}, inplace=True)
        __df['labels'] = __df['labels'].astype(str)

        #
        dataset = Dataset.from_pandas(__df)

        # Function to replace string labels with integers
        def tokenize_function(examples):
            return self.tokenizer(examples["document"], truncation=True, padding="max_length",
                                  max_length=self.max_length,
                                  add_special_tokens=True)

        def map_labels(example):
            example['labels'] = lbl2id[example['labels']]
            return example

        dataset = dataset.map(tokenize_function, batched=True)

        tokenized_datasets = dataset.map(map_labels).remove_columns(['document'])
        tokenized_datasets.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

        return tokenized_datasets

    def load_model(self, model_name_or_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
        if self.label2id and self.id2label:
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path, id2label=self.id2label,
                                                                            label2id=self.label2id,
                                                                            num_labels=len(self.label2id))
        else:
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path)
            self.label2id = self.model.config.label2id
            self.id2label = self.model.config.id2label

        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)

    @staticmethod
    def compute_metrics(eval_pred):
        labels = eval_pred.label_ids
        preds = eval_pred.predictions.argmax(-1)

        # Calculate accuracy
        accuracy = accuracy_score(labels, preds)

        # Calculate precision, recall, and F1-score
        precision = precision_score(labels, preds, average='weighted')
        recall = recall_score(labels, preds, average='weighted')
        f1 = f1_score(labels, preds, average='weighted')

        # logger.info(preds)
        # logger.info(labels)
        # accuracy_topk5 = top_k_accuracy_score(labels, probs, k=5, labels=list(id2label.keys()))

        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            # 'top 5 accuracy': accuracy_topk5
        }

    def predict(self, sentences, top_k=20, batch_size=100):
        pipe = TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer,
                                          truncation=True, padding=True, max_length=self.max_length,
                                          add_special_tokens=True, batch_size=batch_size, top_k=top_k)
        predictions = []
        if isinstance(sentences, pd.DataFrame):
            if self.trainer:
                tokenized_datasets = self.tokenize_preprocess(sentences, self.label2id)
                return self.trainer.predict(tokenized_datasets)
            else:
                inputs_data = Dataset.from_pandas(sentences)
                for out in pipe(KeyDataset(inputs_data, 'document'), batch_size=100, truncation=True, padding=True,
                                max_length=512):
                    predictions.append(out)
                for i in range(len(inputs_data)):
                    # id = inputs_data[i]['id']
                    pred_label = predictions[i][0]['label']
                    pred_prob = predictions[i][0]['score']
                    logger.info(f'{id}: {pred_label} ({pred_prob})')
        elif isinstance(sentences, list) and self.model and self.tokenizer:
            predictions = pipe(sentences, batch_size=100, truncation=True, padding=True, max_length=512)
        else:
            raise Exception("No trainer or model was loaded")

        logger.info(predictions)
        return predictions

    def save_model(self, path):
        if self.trainer:
            self.trainer.save_model(path)
        else:
            raise ValueError("Trainer has not been initialized")

    def train(self, dataset_train, dataset_validation, freeze=False, num_min_freeze=2):
        assert self.training_args, "Trainer args has not been initialized"

        self.freeze(freeze, num_min_freeze)

        train_dataset = self.tokenize_preprocess(dataset_train, self.label2id)
        eval_dataset = self.tokenize_preprocess(dataset_validation, self.label2id)

        self.trainer = Trainer(
            model=self.model,
            args=self.training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=self.tokenizer,
            data_collator=self.data_collator,
            compute_metrics=self.compute_metrics,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
        )

        return self.trainer.train()


class Learner:
    """ Class responsible for learning workflow process
    Attributes:
        embeddings (dict): Embedding models, usually key is the language of the embedding
        recommender (dict): Recommender models, usually key is the hiearchy level of the model
        categorical_encoder (obj): Encoder for categorical features
        categorical_columns (str): Column names for categorical features
        label_encoders (obj): Encoder for labels
    """

    def __init__(self, config, issue_dao, restart=True):
        """ Initializes a Learner instance according to database connection, output dir and model hyperparameters
        Args:
            config (dict): Configuration for learner instance, including database connection,
                           output directories, learning window period and model hyperparameters
        """

        logger.debug(f'Configuration loaded:{json.dumps(config, indent=2)}')

        self.issue_dao = issue_dao
        self.days_interval = int(config['learner_days_interval'])
        self.end_date = config['end_date']
        self.start_date = config['start_date']

        self.model_dir = config['learner_recommender_model_dir']

        if os.path.exists(self.model_dir):
            if restart:
                shutil.rmtree(self.model_dir)
                os.makedirs(self.model_dir)
        else:
            os.makedirs(self.model_dir)

        self.embeddings: Optional[LLMTrainer] = None
        self.issues_train_counts = pd.Series(dtype="int64")
        self.tg_mapping = None

        self.label = config['learner_label']
        self.categorical_columns = config['learner_categorical_columns']
        self.dnn_settings = config['learner_dnn_settings']
        self.test_size = float(config['learner_test_size'])
        self.preprocessor = Preprocessor(config)
        self.model_name_or_path = self.dnn_settings['model']
        self.text_column = "document"

        self.training_args = TrainingArguments(
            output_dir=f'{self.model_dir}/llm/results',  # output directory
            num_train_epochs=self.dnn_settings['num_epochs'],  # total number of training epochs
            per_device_train_batch_size=self.dnn_settings['batch_size'],  # batch size per device during training
            per_device_eval_batch_size=self.dnn_settings['batch_size_eval'],  # batch size for evaluation
            learning_rate=self.dnn_settings['learning_rate'],
            warmup_steps=self.dnn_settings['warmup_steps'],  # number of warmup steps for learning rate scheduler
            weight_decay=self.dnn_settings['weight_decay'],  # strength of weight decay
            load_best_model_at_end=True,  # load the best model when finished training (default metric is loss)
            save_strategy=self.dnn_settings['strategy'],
            fp16=self.dnn_settings['has_fp16'],
            evaluation_strategy=self.dnn_settings['strategy'],  # evaluate each `logging_steps`
            report_to="none",
            metric_for_best_model=self.dnn_settings['eval_metric'],
            label_smoothing_factor=self.dnn_settings['lsf']
        )

    @staticmethod
    def get_labels(dataset_df, l_column):
        # Transforming non numerical labels into numerical labels
        _encoder = LabelEncoder()

        _encoder.fit(dataset_df[l_column].astype(str))

        _encoded_data = _encoder.transform(_encoder.classes_)
        _encoded_data = _encoded_data.tolist()

        _id2label = dict(zip(_encoded_data, _encoder.classes_))
        _label2id = dict(zip(_encoder.classes_, _encoded_data))

        return _label2id, _id2label

    def get_issues(self):
        """ Get data from the configured issue collection and period, and transforms it into a pd.DataFrame
        Returns:
            pd.DataFrame : DataFrame with issue data as defined in MongoDB
        """
        logger.debug('get_issue_dataset')

        if self.end_date is None:
            end = datetime.combine(date.today(), time.max)
        elif isinstance(self.end_date, str):
            end = datetime.strptime(self.end_date, DATE_FORMAT)
            end = datetime.combine(end, time.max)
        else:
            raise ValueError("Invalid end_date. It should be either None or a string in the format 31/12/1999")

        if self.start_date is None:
            if self.days_interval is None:
                raise ValueError('Invalid value. \'start_date\' or \'days_interval\' must be set.')
            days = timedelta(days=self.days_interval)
            start = datetime.combine(end - days, time.min)
        elif isinstance(self.start_date, str):
            start = datetime.strptime(self.start_date, DATE_FORMAT)
            start = datetime.combine(start, time.min)
        else:
            raise ValueError("Invalid start_date. It should be either None or a string in the format 31/12/1999")

        logger.debug(f'get_issue_dataset | start date: {start.strftime("%Y-%m-%d")}')
        logger.debug(f'get_issue_dataset | end date: {end.strftime("%Y-%m-%d")} ')

        return self.issue_dao.find_issues_by_date_and_status(start, end, 'close', 'flat')


    def split_dataset(self, issues, shuffle=False):
        """ Splitting dataset using the last 10% of each label based on datetime
        Args:
            issues (pd.DataFrame): Issues dataset with preprocessed data
            shuffle (bool): Shuffle dataset before splitting
        """
        logger.debug('split_dataset')
        labels = issues[self.label].dropna().unique()
        train, test = [], []
        for label in labels:
            each_class = issues.loc[issues[self.label] == label].index
            if len(each_class) == 1:
                train.append(each_class)
            else:
                train_split, test_split = train_test_split(each_class, shuffle=shuffle, test_size=self.test_size)
                train.append(train_split)
                test.append(test_split)

        _issues_train = issues.loc[np.concatenate(train)]
        _issues_test = issues.loc[np.concatenate(test)]

        self.issues_train_counts = _issues_train[self.label].value_counts()

        logger.debug(f'split_dataset | {len(_issues_test)} issues saved for test')
        logger.debug(f'split_dataset | {len(_issues_train)} issues used to train model')

        return _issues_train, _issues_test

    def train(self, issues_train, issues_test):
        logger.debug('Train embedding supervised')

        train = issues_train[['document', self.label]]
        test = issues_test[['document', self.label]]

        # TRAINING PROCESS
        _label2id, _id2label = self.get_labels(issues_train, self.label)
        logger.debug(_label2id)
        self.training_args.output_dir = f'{self.model_dir}/results'
        _trainer = LLMTrainer(model_name_or_path=self.model_name_or_path, text_column=self.text_column,
                              label_column=self.label, label2id=_label2id, id2label=_id2label,
                              training_args=self.training_args)

        logger.info(train.shape)
        logger.info(test.shape)
        _trainer.train(dataset_train=train, dataset_validation=test)
        self.embeddings = _trainer

        # Get the mapping from id to names
        tg_mapping = issues_train[['tg_solver_id', 'tg_solver_full_name']].drop_duplicates()
        tg_mapping.index = tg_mapping['tg_solver_id']
        tg_mapping = tg_mapping.to_dict()

        self.tg_mapping = tg_mapping['tg_solver_full_name']

    def save_models(self, issues_test):
        """ Save models to the directory configured in self.model_dir
        """
        logger.debug('save_models')

        __name = final_model_name(self.model_name_or_path)
        self.embeddings.save_model(os.path.join(self.model_dir, __name))
        shutil.rmtree(self.training_args.output_dir)

        pickle.dump(self.tg_mapping, open(os.path.join(self.model_dir, 'tg_mapping.pkl'), 'wb'))
        issues_test.to_pickle(os.path.join(self.model_dir, 'issues_test.pkl'))
        self.issues_train_counts.to_csv(os.path.join(self.model_dir, 'issues_train_counts.csv'))

    def predict(self, issues_df, top_k=1):
        logger.debug('predict')

        test = issues_df[['document', self.label]]
        results = self.embeddings.predict(test, top_k)
        return results

    # def evaluate(self, issues_df):
    #     logger.debug('evaluate')
    #
    #     test = issues_df[['document', self.label]]
    #     results = self.embeddings[l].evaluator(test)
    #     return results

    def start_workflow(self):
        """ Run the complete learning workflow according to the configured parameters
        """
        issues = self.get_issues()
        issues = self.preprocessor.preprocess_issues(issues)

        issues_train, issues_test = self.split_dataset(issues)
        issues_train, issues_validation = self.split_dataset(issues_train, shuffle=True)

        self.train(issues_train, issues_validation)
        self.save_models(issues_test)
