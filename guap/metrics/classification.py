# -*- coding: utf-8 -*-

from statistics import mean
from typing import Any, Dict, List

import numpy as np
from loguru import logger
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder


def guap_cm(y_true: List[int], y_pred: List[int]) -> List[List[int]]:
    """Generate confusion matrix based on true and predicted labels.

    Parameters
    ----------
    y_true : List[int]
        List of true labels
    y_pred : List[int]
        List of predicted labels

    Returns
    -------
    List[List[int]]
        Confusion matrix
    """
    # TODO: maybe get rid of sklearn dependence?
    cm = confusion_matrix(y_true, y_pred)

    return cm


def _format_labels(y_list: List[int], label: int) -> List[int]:
    """A useful function to transform a multiclassification problem to
    a binary classification by mapping `label` input to 1 and other labels to 0.

    Parameters
    ----------
    y_list : List[int]
        List of labels to transform
    label : int
        Input label to consider as positive class

    Returns
    -------
    List[int]
        New list of labels transformed into binary labels
    """
    output = [1 if y == label else 0 for y in y_list]

    return output


def _formula(cm: List[List[int]], cost_matrix: List[List[float]]) -> float:
    """Aggregate the total cost using the generated confusion matrix and the
    given cost matrix

    Parameters
    ----------
    cm : List[List[int]]
        Generated confusion matrix
    cost_matrix : List[List[float]]
        Given cost matrix in the form of [[TN, FP], [FN, TP]]

    Returns
    -------
    float
        The total cost
    """
    score = (cm * cost_matrix).sum()

    return score


def _cost_matrix_check(matrix: List[List[float]]) -> None:
    """Ensure the cost matrix format. The size should be equal to (2, 2) matrix.

    Parameters
    ----------
    matrix : List[List[float]]
        Any matrix format

    Raises
    ------
    AssertError
        If the input matrix size doesn't satisfy the condition
    """
    assert np.array(matrix) == (2, 2), "The cost matrix size should be equal to (2, 2)"


def guap_metric(
    y_true: List[int], y_pred: List[int], cost_matrix: List[List[float]]
) -> Dict[str, float]:
    """Compute the Guap metric for a multiclassification problem giving the
    list of true labels, predicted labels and cost matrix.

    Parameters
    ----------
    y_true : List[int]
        List of true labels.
    y_pred : List[int]
        List of predicted labels by the model to evaluate.
    cost_matrix : List[List[float]]
        Given cost matrix.

    Returns
    -------
    Dict[str, float]
        The average and total cost.
    """
    # _cost_matrix_check(cost_matrix)
    le = LabelEncoder()
    y_true_encoded = le.fit_transform(y_true)
    y_pred_encoded = le.transform(y_pred)
    labels = le.transform(le.classes_)
    results = {}
    for i, label in enumerate(labels):
        binary_y_true = _format_labels(y_true_encoded, label)
        binary_y_pred = _format_labels(y_pred_encoded, label)
        cm = guap_cm(binary_y_true, binary_y_pred)
        results[le.classes_[i]] = _formula(cm, cost_matrix)
    _tmp = sum(results.values())
    output = {"sum": sum(results.values()), "average": mean(results.values())}

    return output


def binary_guap_metric(
    y_true: List[int], y_pred: List[int], cost_matrix: List[List[float]]
) -> float:
    """Computer the Guap metric for binary classification problem giving the
    list of true labels, predicted labels and cost matrix.

    Parameters
    ----------
    y_true : List[int]
        List of true labels.
    y_pred : List[int]
        List of predicted labels by the model to evaluate.
    cost_matrix : List[List[float]]
        Given cost matrix.

    Returns
    -------
    float
        Total cost
    """
    le = LabelEncoder()
    y_true_encoded = le.fit_transform(y_true)
    y_pred_encoded = le.transform(y_pred)
    labels = le.transform(le.classes_)
    cm = guap_cm(y_true_encoded, y_pred_encoded)
    score = _formula(cm, cost_matrix)

    return score
