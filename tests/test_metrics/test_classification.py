# -*- coding: utf-8 -*-

from guap.metrics import guap_metric


def test_guap_metric():
    output = guap_metric([1], [2])
    assert output == "Done"
