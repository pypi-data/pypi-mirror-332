"""
Module that implements class responsible for sample prediction

@author fabiano.tavares
"""
import json
import os
import pickle
import shutil
import tarfile
from typing import Dict

import numpy as np
import pandas as pd
from loguru import logger

from .learner import LLMTrainer, final_model_name
from .preprocessor import Preprocessor


class Predictor:
    """ Class responsible for performing training-dependant preprocessing (labels,)

    Attributes:
        embeddings (dict): Embedding models, usually key is the language of the embedding
        recommender (dict): Recommender models, usually key is the hiearchy level of the model
        categorical_encoder (obj): Encoder for categorical features
        categorical_columns (str): Column names for categorical features
        label_encoders (obj): Encoder for labels
        model_loaded_ (boolean): Boolean to indicate whether the models are loaded
    """

    def __init__(self, config):
        """ Initializes a Learner instance according to database connection, output dir and model hyperparameters

        Args:
            config (dict): Configuration for learner instance, including database connection,
                           output directories, learning window period and model hyperparameters
        """

        logger.debug(f'Configuration loaded:{json.dumps(config, indent=2)}')

        self.model_dir = config['learner_recommender_model_dir']
        self.model_name_or_path = config['learner_dnn_settings']['model']

        self.model_loaded_ = False
        self.model_reported_ = False

        self.recommender: LLMTrainer = None
        self.tg_mapping = None
        self.label = config['learner_label']
        self.text_column = "document"

        self.report_top_k = pd.DataFrame()
        self.report_totals = pd.DataFrame()
        self.tops_k = config['validator_top_k']
        self.issues_train_counts = pd.Series(dtype="int64")

        self.preprocessor = Preprocessor(config)

    def load_binaries(self):
        if os.path.exists(self.model_dir):
            __name_path = os.path.join(self.model_dir, final_model_name(self.model_name_or_path))
            logger.debug(__name_path)
            self.recommender = LLMTrainer(__name_path, text_column=self.text_column, label_column=self.label)

            self.tg_mapping = pickle.load(open(os.path.join(self.model_dir, 'tg_mapping.pkl'), 'rb'))
            self.issues_train_counts = pd.read_csv(os.path.join(self.model_dir, 'issues_train_counts.csv'), index_col=0)
            self.model_loaded_ = True

    def load_models(self, tar_file):
        """ Load embeddings, encoders and recommender models from the directory configured in self.model_dir
        """
        if tar_file and tarfile.is_tarfile(tar_file):
            if os.path.exists(self.model_dir):
                shutil.rmtree(self.model_dir)
            os.makedirs(self.model_dir)
            tar = tarfile.open(tar_file)
            tar.extractall(self.model_dir)
            tar.close()
        else:
            raise TypeError('Input file is not a tar file')

        if os.path.exists(self.model_dir):
            self.load_binaries()

            report_file = os.path.join(self.model_dir, 'report_top_k.csv')
            if os.path.exists(report_file):
                self.report_top_k = pd.read_csv(report_file,
                                                index_col="classes")
                self.report_totals = self.report_top_k.loc["TOTALS"]
                self.report_top_k = self.report_top_k.drop("TOTALS")
                self.model_reported_ = True

            logger.debug('Model loaded')
        else:
            raise FileNotFoundError('Model input file does not exist')

    def predict(self, issues, top_predictions=0, process_issues=True):
        """ Recommends most likely TGs that must be assigned to a list of issues
        Args:
            issue (list): Issues that must be assigned to TGs
            top_predictions (int): Maximmum number of TGs that may be predicted to the issues
            process_issues (boolean): whether to process issues or not
        Returns:
            List of elements in the format [(class_name, probability), ...] sorted by probability
            in the descending order
        """
        if self.model_loaded_:
            logger.debug('predict')
            issues = pd.DataFrame(issues)

            if process_issues:
                issues = self.preprocessor.preprocess_issues(issues)

            top_pred_ret = []
            for _, row in issues.iterrows():
                doc = row['document']
                rank = self.recommender.predict([doc], top_k=top_predictions)
                top_pred_ret.append(rank[0])

            return top_pred_ret
        else:
            return [[]]

    def get_label_details(self) -> dict:
        """ Create a evaluation of test split using a TG information with top k items
        """
        if self.model_reported_:
            tg_mapper = np.vectorize(
                lambda tg_id: self.tg_mapping[int(float(tg_id))])

            top_classes_names = tg_mapper(self.report_top_k.index)
            top_classes_names = top_classes_names.tolist()
            tg_details = {}
            for i, classes in enumerate(top_classes_names):
                predicted_class_path = classes.split("->")
                tg = self.report_top_k.iloc[i]
                tg_detail = {
                    "id":
                        int(float(tg.name)),
                    "name":
                        predicted_class_path[-1],
                    "path":
                        predicted_class_path[:-1],
                    "train_size":
                        int(self.issues_train_counts.loc[int(float(tg.name))]),
                    "test_size":
                        int(tg['expect_length_1']),
                }
                for k in self.tops_k:
                    tops = {
                        f"top{k}_accuracy": tg[f'accuracy_{k}'],
                        f"top{k}_hits": int(tg[f'hits_{k}']),
                        f"top{k}_mrr": tg[f'mrr_{k}'],
                        f"top{k}_precision": tg[f'precision_{k}'],
                        f"top{k}_recall": tg[f'recall_{k}'],
                        f"top{k}_fmeasure": tg[f'f1-score_{k}'],
                    }
                    tg_detail.update(tops)
                tg_details[int(float(tg.name))] = tg_detail
            return tg_details
        return {}

    def get_dataset_details(self) -> dict:
        """ Evaluation of the whole dataset
        """
        if self.model_reported_:
            dataset_details = {
                "train_size": int(self.issues_train_counts.sum()),
                "test_size": int(self.report_totals['expect_length_1']),
            }
            for k in self.tops_k:
                tops = {
                    f"top{k}_accuracy": self.report_totals[f'accuracy_{k}'],
                    f"top{k}_hits": int(self.report_totals[f'hits_{k}']),
                    f"top{k}_mrr": int(self.report_totals[f'mrr_{k}']),
                    f"top{k}_precision": self.report_totals[f'precision_{k}'],
                    f"top{k}_recall": self.report_totals[f'recall_{k}'],
                    f"top{k}_fmeasure": self.report_totals[f'f1-score_{k}'],
                }
                dataset_details.update(tops)
            return dataset_details
        return {}