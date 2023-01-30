#!/usr/bin/env python
import datetime
import re

from enum import Enum


__all__ = ["toggle_case", "camel_case", "snake_case", "spinal_case", "pascal_case"]


class CaseType(Enum):
    UPPER = "UPPER"
    LOWER = "LOWER"
    Capitalize = "Capitalize"
    Camel = "Camel"
    Snake = "Snake"
    Spinal = "Spinal"
    Pascal = "Pascal"


def toggle_case(string, case_type: CaseType = CaseType.LOWER):
    if case_type == CaseType.UPPER:
        return str(string).upper()
    elif case_type == CaseType.LOWER:
        return str(string).lower()


def camel_case(string: str) -> str:
    string = re.sub(r"^[\-_\.]", "", str(string))
    if not string:
        return string
    return toggle_case(string[0], CaseType.LOWER) + re.sub(
        r"[\-_\.\s]([a-z])",
        lambda matched: toggle_case(matched.group(1), CaseType.UPPER),
        string[1:],
    )
    # return "".join(word.capitalize() for word in string.split("_"))


# def to_camel(string: str) -> str:
#     return "".join(word.capitalize() for word in string.split("_"))


def snake_case(string):
    """Convert string into snake case.
    Join punctuation with underscore

    Args:
        string: String to convert.

    Returns:
        string: Snake cased string.

    """

    string = re.sub(r"[\-\.\s]", "_", str(string))
    if not string:
        return string
    return toggle_case(string[0], CaseType.UPPER) + re.sub(
        r"[A-Z]",
        lambda matched: "_" + toggle_case(matched.group(0), CaseType.LOWER),
        string[1:],
    )


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


def str_to_datetime(value, fmt="%Y-%m-%d %H:%M:%S"):
    """时间类型转换为字符串。datetime to string.

    :type value: str
    :type fmt: str
    :rtype: datetime.datetime
    """
    return datetime.datetime.strptime(value, fmt)


def str_to_date(value, fmt="%Y-%m-%d"):
    """日期类型转换为字符串。date to string.

    :type value: str
    :type fmt: str
    :rtype: datetime.date
    """
    return datetime.datetime.strptime(value, fmt).date()


def bytes_to_str(data):
    """二进制类型转换为字符串，支持嵌套数组。bytes to string, supports nested list.

    Examples::

        string_value = bytes_to_str(redis.get('key'))
        values = bytes_to_str(redis.mget(*keys))
    """
    if data is None:
        return data
    if isinstance(data, bytes):
        return data.decode()
    if isinstance(data, str):
        return data
    return [bytes_to_str(_) for _ in data]
