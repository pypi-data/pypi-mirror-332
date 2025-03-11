from .predictor import Predictor
from .utils.confusion_matrix import ConfusionMatrix
import os
import logging
import pandas as pd
import numpy as np
from functools import reduce

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)s) %(message)s",
)
logger = logging.getLogger("Validator")


class Validator:
    """ Class responsible for validation and deploy model in minio server.
    """

    def __init__(self, config):
        """ Initializes a Learner instance according to database connection, output dir and model hyperparameters

        Args:
            config (dict): Configuration for learner instance, including database connection,
                           output directories, learning window period and model hyperparameters
        """
        self.model_dir = config['learner_recommender_model_dir']
        self.tops_k = config['validator_top_k']

        self.predictor = Predictor(config)
        self.predictor.load_binaries()

        self.issues_test_loaded = False
        self.evaluated = False
        self.issues_test, self.issues_y_test = self.__get_issues_test()

    def __get_issues_test(self):
        """ Get issues test from a file to evaluate
        """
        issue_test_file = os.path.join(self.model_dir, 'issues_test.pkl')
        issues_test = pd.read_pickle(issue_test_file)
        y_test = issues_test[self.predictor.label].to_numpy(dtype=np.int64)
        os.remove(issue_test_file)
        self.issues_test_loaded = True
        return issues_test, y_test

    def evaluate(self):
        """ Generate metrics to evaluate TG perfomance
        """
        logger.debug('evaluate')

        y_pred = np.squeeze(self.predictor.predict(self.issues_test, self.tops_k[-1], False))
        y_pred_top_k = []
        for pred in y_pred:
            y_pred_top_k.append(list(map(lambda elem: elem['label'], pred)))

        y_pred_top_k = np.array(y_pred_top_k, dtype=np.int64)

        classes = list(self.predictor.tg_mapping.keys())

        reports = []
        for k in self.tops_k:
            classifier_matrix = ConfusionMatrix(classes, precision_zero_division=0.0)
            classifier_matrix.set_predictions(self.issues_y_test, y_pred_top_k[:, :k])
            classifier_report = classifier_matrix.describe(expect_length=1)
            classifier_report.columns = list(map(lambda column: f"{column}_{k}", classifier_report.columns))
            reports.append(classifier_report)

        report = reduce(
            lambda left, right: pd.merge(
                left, right, on=['classes'], how='inner'), reports)
        report.to_csv(os.path.join(self.model_dir, 'report_top_k.csv'))

        self.evaluated = True
        logger.debug('evaluate: Created a metric report of TGs')
