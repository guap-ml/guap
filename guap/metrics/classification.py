# -*- coding: utf-8 -*-

from statistics import mean
from typing import Any, Dict, List

import numpy as np
from loguru import logger
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder


def guap_cm(y_true: List[int], y_pred: List[int]) -> List[List[int]]:
    # TODO: maybe get rid of sklearn dependence?
    cm = confusion_matrix(y_true, y_pred)

    return cm


def _format_labels(y_list: List[int], label: int) -> List[int]:
    output = [1 if y == label else 0 for y in y_list]

    return output


def _formula(cm: List[List[int]], cost_matrix: List[List[float]]) -> float:
    # score = np.dot(cm, cost_matrix).sum()
    score = (cm * cost_matrix).sum()

    return score


def _cost_matrix_check(matrix: List[List[float]]) -> None:
    assert np.array(matrix) == (2, 2), "The cost matrix size should be equal to (2, 2)"


def guap_metric(
    y_true: List[int], y_pred: List[int], cost_matrix: List[List[float]]
) -> Dict[str, float]:
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
    le = LabelEncoder()
    y_true_encoded = le.fit_transform(y_true)
    y_pred_encoded = le.transform(y_pred)
    labels = le.transform(le.classes_)
    cm = guap_cm(y_true_encoded, y_pred_encoded)
    score = _formula(cm, cost_matrix)

    return score
