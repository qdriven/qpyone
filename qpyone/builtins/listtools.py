#!/usr/bin/env python
from typing import Any
from typing import List


def flat(nested_list: list[list[Any]]):
    result = []
    for list_item in nested_list:
        for item in list_item:
            if item is not None:
                result.append(item)

    return result
