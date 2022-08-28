#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
import re
from enum import Enum


class CaseType(Enum):
    UPPER = "UPPER"
    LOWER = "LOWER"
    Capitalize = "Capitalize"
    Camel = "Camel"
    Snake = "Snake"
    Spinal = "Spinal"
    Pascal = "Pascal"


def upper_or_lower(string, case_type: CaseType = CaseType.LOWER):
    if case_type == CaseType.UPPER:
        return str(string).upper()
    elif case_type == CaseType.LOWER:
        return str(string).lower()


def camel_case(string):
    string = re.sub(r"^[\-_\.]", '', str(string))
    if not string:
        return string
    return (upper_or_lower(string[0], CaseType.LOWER)
            + re.sub(r"[\-_\.\s]([a-z])",
                     lambda matched: upper_or_lower(matched.group(1), CaseType.UPPER),
                     string[1:]))


def snake_case(string):
    """Convert string into snake case.
    Join punctuation with underscore

    Args:
        string: String to convert.

    Returns:
        string: Snake cased string.

    """

    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return (upper_or_lower(string[0], CaseType.UPPER)
            + re.sub(r"[A-Z]",
                     lambda matched: '_' + upper_or_lower(matched.group(0),
                                                          CaseType.LOWER),
                     string[1:]))


def spinal_case(string):
    """Convert string into spinal case.
    Join punctuation with hyphen.

    Args:
        string: String to convert.

    Returns:
        string: Spinal cased string.

    """

    return re.sub(r"_", "-", snake_case(string))


def pascal_case(string):
    """Convert string into pascal case.

    Args:
        string: String to convert.

    Returns:
        string: Pascal case string.

    """

    return camel_case(string).capitalize()


## todo: use funtools partial func to re-org functions
case_function_map = {
}
