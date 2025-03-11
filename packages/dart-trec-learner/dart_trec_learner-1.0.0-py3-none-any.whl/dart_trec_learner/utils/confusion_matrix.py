'''
Copyright 2017-2027 SIDIA. All rights reserved.

Implementation of Confusion Matrix: row is expected, columns is actual

@author fabricio.dm
@version 1.00.00 - Aug 07, 2017 - fabricio.dm - initial version.
'''
import numpy as np
import pandas as pd
from tabulate import tabulate


class ConfusionMatrix:
    def __init__(self,
                 classes: list,
                 name: str = None,
                 precision_zero_division=1.0,
                 recall_zero_division=0.0,
                 accuracy_zero_division=1.0,
                 decimals=4):
        """
        Args:
            classes (list): A list of classes to evaluate
            name (str): Identification for the matrix
        Returns:
            list: A list of classes.
        """
        self.name = name
        self.classes = classes
        self.shape = None
        self.matrix = None

        self.precision_zero_division = precision_zero_division
        self.recall_zero_division = recall_zero_division
        self.accuracy_zero_division = accuracy_zero_division
        self.decimals = decimals

        # Store the amount of times that the expected TG is in the recommendation rank
        self.true_positives = {clazz: 0 for clazz in self.classes}
        self.false_positives = {clazz: 0 for clazz in self.classes}
        self.false_negatives = {clazz: 0 for clazz in self.classes}
        self.mrr = {clazz: [] for clazz in self.classes}

    def clone(self):
        '''
        Clones this confusion matrix (deep copy)
        Returns:
            ConfusionMatrix: returns a copy of this matrix.
        '''
        copy = ConfusionMatrix(self.classes, name=self.name)
        copy.combine_with([self])
        return copy

    def __str__(self):
        return self.to_string()

    def to_string(self, fmt="fancy_grid"):
        """
        Generates a tabular string representation of the confusion matrix
        Args:
            fmt: The string format to render the matrix. Default: fancy_grid.
                 Options: plain, simple, github, grid, fancy_grid, pipe, orgtbl, jira, presto, psql, rst, mediawiki,
                 moinmoin, youtrack, html, latex, latex_raw, latex_booktabs, textile
        Returns:
            str: The string representation of the matrix.
        """
        headers = [i for i in range(len(self.matrix.columns))]
        return tabulate(self.matrix, headers=headers, tablefmt=fmt)

    def set_predictions(self, expected_classes: list, ranks: list):
        '''
        Set many prediction in the matrix at once
        '''

        self.__create_confusion_matrix(ranks)

        for expected, rank in zip(expected_classes, ranks):
            predicted = rank[0]

            # We evaluate only the TGs specified in classes
            if expected not in self.classes:
                return

            self.matrix.loc[expected, predicted] += 1

            tp_index = [
                idx_pred for idx_pred, pred in enumerate(rank)
                if pred == expected
            ]
            TP = len(tp_index)
            FP = len(rank) - TP
            FN = 0 if TP else 1
            MRR = 1 / (tp_index[0] + 1) if tp_index else 0

            self.true_positives[expected] += TP
            self.false_positives[expected] += FP
            self.false_negatives[expected] += FN
            self.mrr[expected].append(MRR)

    # TODO - I don't know if this confusion matrix still makes sense
    # since we refactored the precision calculation.
    # Arthur Batista
    def __create_confusion_matrix(self, ranks):
        columns = set(ranks[:, 0])
        columns.update(self.classes)
        self.shape = (len(self.classes), len(columns))
        self.matrix = pd.DataFrame(np.zeros(self.shape, dtype=np.int64),
                                   index=self.classes,
                                   columns=list(columns))
        self.matrix.index.name = self.name

    def get_class_expected_length(self, clazz):
        '''
        Returns:
            int: The class original length before classification
        '''
        return self.true_positives[clazz] + self.false_negatives[clazz]

    def get_class_prediction_length(self, clazz):
        '''
        Returns:
            int: The class resulting length after classification
        '''
        return self.matrix[clazz].sum()

    def length(self):
        '''
        Returns:
            int: The quantity of classified instances
        '''
        return sum(self.true_positives.values()) + sum(
            self.false_negatives.values())

    def non_hits(self, clazz):
        '''
        Returns:
            int: The quantity of incorrectly classified instances
        '''
        return self.get_class_expected_length(
            clazz) - self.true_positives[clazz]

    def false_discovery(self, clazz):
        '''
        Returns:
            int: The quantity of incorrectly discovered instances
        '''
        return self.get_class_prediction_length(clazz) - self.true_positives(
            clazz)

    def get_mrr(self, clazz):
        '''
        Returns:
            float: The classification precision for a single class
        '''
        mrr = self.mrr[clazz]
        result = sum(mrr) / len(mrr) if mrr else 0
        return round(result, self.decimals)

    def accuracy(self, include: list = None, exclude: list = None):
        '''
        Returns:
            float: The classification accuracy
        '''
        hits = 0
        size = 0
        classes = set(self.classes)
        if include is not None:
            classes = classes.intersection(include)
        if exclude is not None:
            classes = classes.difference(exclude)
        for clazz in classes:
            hits += self.true_positives[clazz]
            size += self.true_positives[clazz] + self.false_negatives[clazz]
        result = hits / size if size > 0 else self.accuracy_zero_division
        return round(result, self.decimals)

    def precision(self, clazz):
        '''
        Returns:
            float: The classification precision for a single class
        '''
        TP = self.true_positives[clazz]
        FP = self.false_positives[clazz]
        result = TP / (TP + FP) if (TP +
                                    FP) > 0 else self.precision_zero_division
        return round(result, self.decimals)

    def recall(self, clazz):
        '''
        Returns:
            float: The classification recall for a single class
        '''
        TP = self.true_positives[clazz]
        FN = self.false_negatives[clazz]
        result = TP / (TP + FN) if (TP + FN) > 0 else self.recall_zero_division
        return round(result, self.decimals)

    def fscore(self, clazz):
        '''
        Returns:
            float: The classification f-score for a single class
        '''
        p = self.precision(clazz)
        r = self.recall(clazz)
        result = 2.0 * (p * r) / (p + r) if (p + r) > 0 else 0.0
        return round(result, self.decimals)

    def false_discovery_rate(self, clazz):
        '''
        Returns:
            int: The rate of incorrectly discovered instances
        '''
        fd = self.false_discovery(clazz)
        size = self.get_class_prediction_length(clazz)
        result = fd / size if size > 0 else 0.0
        return round(result, self.decimals)

    def growth(self, clazz):
        '''
        Returns:
            float: How much a class increased or decreased its size. No modification is denoted by 1.
        '''
        expected = self.get_class_expected_length(clazz)
        actual = self.get_class_prediction_length(clazz)
        result = actual / expected if expected > 0 else 1.0
        return round(result, self.decimals)

    def describe(self,
                 order_by=None,
                 ascending=False,
                 precision=0,
                 recall=0,
                 fscore=0,
                 expect_length=0,
                 predict_length=0,
                 hits=0):
        '''
        Generate descriptive statistics that summarize the confusion matrix.
        Also, it selects classes which has evaluation greater then provided thresholds.
        Args:
            order_by (list): A list of metrics. Default: [fscore, recall, precision].
            ascending (bool): order by ascending, otherwise descending.
            precision (float): Lower threshold for precision.
            recall (float): Lower threshold for recall.
            fscore (float): Lower threshold for fscore.
            expect_length (float): Lower threshold for expect_length. When in [0,1] range,
                                                threshold is replaced by length quantile.
            predict_length (float): Lower threshold for predict_length. When in [0,1] range,
                                                threshold is replaced by length quantile.
            hits (int): Lower threshold for hits.
        Returns:
            pd.DataFrame: a table of evaluation per class.
        '''
        # Calculate evaluation metrics both global and per class
        col_labels = [
            "expect_length", "predict_length", "hits", "mrr", "accuracy",
            "precision", "recall", "f1-score", "growth"
        ]

        order_by = ["recall", "precision", "f1-score"
                    ] if order_by is None else order_by
        mrr = 0
        accuracy = 0

        # Per class evaluations
        class_evaluation = [
            (self.get_class_expected_length(clazz),
             self.get_class_prediction_length(clazz),
             self.true_positives[clazz], self.get_mrr(clazz), accuracy,
             self.precision(clazz), self.recall(clazz), self.fscore(clazz),
             self.growth(clazz)) for clazz in self.classes
        ]
        class_evaluation = pd.DataFrame(class_evaluation,
                                        index=self.classes,
                                        columns=col_labels)
        class_evaluation.sort_values(by=order_by,
                                     ascending=ascending,
                                     inplace=True)

        # If length threshold is a quantile, set length to value at quantile
        if isinstance(expect_length, float) and (0.0 <= expect_length < 1.0):
            expect_length = class_evaluation["expect_length"].quantile(
                expect_length)
        if isinstance(predict_length, float) and (0.0 <= predict_length < 1.0):
            predict_length = class_evaluation["predict_length"].quantile(
                predict_length)

        # Filter class evaluations
        class_evaluation_filtered = class_evaluation[
            (class_evaluation["mrr"] >= mrr)
            & (class_evaluation["precision"] >= precision) &
            (class_evaluation["recall"] >= recall) &
            (class_evaluation["f1-score"] >= fscore) &
            (class_evaluation["expect_length"] >= expect_length) &
            (class_evaluation["predict_length"] >= predict_length) &
            (class_evaluation["hits"] >= hits)]

        # Measure accuracy based on filtered classes
        accuracy = self.accuracy(include=list(class_evaluation_filtered.index))
        class_evaluation_filtered["accuracy"] = accuracy

        # Total evaluations
        total_evaluation = [
            (class_evaluation["expect_length"].sum(),
             class_evaluation["predict_length"].sum(),
             class_evaluation["hits"].sum(),
             round(class_evaluation_filtered["mrr"].mean(),
                   self.decimals), accuracy,
             round(class_evaluation_filtered["precision"].mean(),
                   self.decimals),
             round(class_evaluation_filtered["recall"].mean(), self.decimals),
             round(class_evaluation_filtered["f1-score"].mean(),
                   self.decimals),
             round(class_evaluation_filtered["growth"].mean(), self.decimals))
        ]
        total_evaluation = pd.DataFrame(total_evaluation,
                                        index=["TOTALS"],
                                        columns=col_labels)

        # Merge both evaluations into one table
        result = pd.concat([total_evaluation, class_evaluation_filtered])
        result.index.name = "classes"
        return result

    def combine_with(self, matrices: list):
        '''
        Combines this matrix with other matrices by summing their values. All matrices should have sames classes.
        Args:
            matrices: The other confusion matrices
        Returns:
            ConfusionMatrix: returns this matrix.
        '''
        for i, other in enumerate(matrices):
            if self.shape != other.shape:
                raise AttributeError(
                    "Matrix %s should have same size than main matrix" % i)
            all_tmp = [c1 == c2 for c1, c2 in zip(self.classes, other.classes)]
            if not all(all_tmp):
                raise AttributeError(
                    "Matrix %s should have same classes than main matrix" % i)
            self.matrix = self.matrix + other.matrix
        return self
