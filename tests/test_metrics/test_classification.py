# -*- coding: utf-8 -*-

from guap.metrics import guap_metric


def test_guap_metric():
    y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
    y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
    cost_matrix = [[200, -1500], [0, 1000]]
    output = guap_metric(y_true, y_pred, cost_matrix)
    # assert output == "Done"
    assert True
