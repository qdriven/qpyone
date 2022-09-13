#!/usr/bin/env python
from qpyone.builtins import listtools


def test_flat():
    result = listtools.flat([[1, 2, 3], ["test", "test"]])
    assert result == [1, 2, 3, "test", "test"]
