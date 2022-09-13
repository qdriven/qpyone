#!/usr/bin/env python
# -*- coding:utf-8 -*-
from fluentqpy.builtins import listtools


def test_flat():
    result = listtools.flat([[1, 2, 3], ["test", "test"]])
    assert result == [1, 2, 3, 'test', 'test']
