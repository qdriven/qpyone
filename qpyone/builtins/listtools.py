#!/usr/bin/env python
from typing import Any
from typing import Iterable


__all__ = ["flat"]


def list_first(instances: Iterable, default=None):
    """获取列表的第一个元素，假如没有第一个元素则返回默认值。get first value of a list or default value.

    Examples::

        list_first(instances)
        # None
    """
    return list_get(instances, 0, default=default)


def list_get(instances: Iterable, index: int, default=None):
    """根据索引号获取列表值或者默认值。get default value on index out of range for list.

    Examples::

        list_get([0, 1, 2], 3, 4)
        # 4
    """
    try:
        return list(instances)[index]
    except IndexError:
        return default


def flat(nested_list: list[list[Any]]) -> list:
    result = []
    for list_item in nested_list:
        for item in list_item:
            if item is not None:
                result.append(item)

    return result
