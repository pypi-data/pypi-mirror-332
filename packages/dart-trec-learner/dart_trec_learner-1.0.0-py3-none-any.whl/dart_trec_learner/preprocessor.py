"""
Module that implements class responsible for issue preprocessing

@author paulo.fonseca
"""
import json
import re

import pandas as pd
from loguru import logger


class Preprocessor:
    """ Class responsible for performing preprocessing
    """

    regex = re.compile(r'\b\w+\b|[.,]')

    def __init__(self, config):
        """ Initializes a Learner instance according to database connection, output dir and model hyperparameters
        Args:
            config (dict): Configuration for learner instance, including database connection,
                           output directories, learning window period and model hyperparameters
        """
        logger.debug(f'Configuration loaded:{json.dumps(config, indent=2)}')

        self.label = config['learner_label']
        self.textual_columns = config['learner_textual_columns']
        self.categorical_columns = config['learner_categorical_columns']
        self.min_issues = config['min_issues']

    def preprocess_document(self, text: str):
        tokens = re.findall(self.regex, text)
        return " ".join(tokens).lower()

    # Function to preprocess a batch of documents
    def preprocess_document_batch(self, df: pd.DataFrame, text_column_name: str) -> pd.DataFrame:
        df[text_column_name] = df[text_column_name].apply(self.preprocess_document)
        return df

    def preprocess_issues(self, issues):
        """ Preprocess issue dataset for further training
            Transforms the issue dataset from the format provided by MongoDB into a format ML-friendly
        Args:
            issues (pd.DataFrame): Issues dataframe with data to be preprocessed
        Returns:
            pd.DataFrame: Preprocessed issues dataframe
        """
        logger.debug('preprocess_issues')

        # Drop issues without TG_SOLVER_ID
        if 'tg_solver_id' in issues.columns:
            issues.dropna(subset=['tg_solver_id'], inplace=True)
            issues['tg_solver_id'] = issues['tg_solver_id'].astype(int)
            issues['tg_solver_full_name'] = issues['tg_solver_full_name'].apply(
                lambda x: '->'.join(x))

        # Change other languages to either KO or EN
        issues['document_lang'].replace('zh', 'ko', inplace=True)

        langs_to_replace = {l: 'en' for l in issues.loc[
            ~(issues['document_lang'] == 'en') & ~(issues['document_lang'] == 'ko'), 'document_lang'].unique().tolist()}

        logger.debug(f'langs_to_replace: {langs_to_replace}')
        issues['document_lang'].replace(langs_to_replace, inplace=True)

        # Create document att by concat textual and categorical
        issues.loc[:, self.categorical_columns].fillna(value='', inplace=True)

        columns = self.textual_columns  # + self.categorical_columns

        logger.debug(f'columns: {columns}')
        issues = issues.assign(document=issues[columns].apply(
            lambda row: ', '.join([str(row[col]) for col in columns]), axis=1))

        issues = self.preprocess_document_batch(issues, "document")
        # .agg(' '.join, axis=1)

        # Columns to keep
        columns_to_keep = ['create_date', 'status', 'document', 'document_lang']

        if 'tg_solver_id' in issues.columns:
            columns_to_keep.extend(['tg_solver_id', 'tg_solver_name', 'tg_solver_full_name'])

        issues = issues[issues['tg_solver_name'].notna() & (issues['tg_solver_name'] != '')]
        issues = issues.groupby('tg_solver_name').filter(lambda x: len(x) >= self.min_issues)

        issues = issues[columns_to_keep].reset_index()

        return issues


