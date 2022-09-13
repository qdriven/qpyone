#!/usr/bin/env python
from qpyone.builtins import stringtools
from qpyone.builtins.stringtools import CaseType


def test_case_upper_or_lower():
    t = stringtools.upper_or_lower("test", CaseType.UPPER)
    assert t == "TEST"
    print("capitalize".capitalize())


def test_camel_case():
    t = stringtools.camel_case("test_case")
    assert t == "testCase"


def test_snake_case():
    t = stringtools.snake_case("test_case")
    assert t == "Test_case"


def test_spinal_case():
    t = stringtools.spinal_case("test_case")
    assert t == "Test-case"


def test_pascal_case():
    t = stringtools.pascal_case("test_case")
    assert t == "Testcase"
