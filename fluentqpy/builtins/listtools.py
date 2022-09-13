#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List, Any


def flat(nested_list: List[List[Any]]):
    result = []
    for list_item in nested_list:
        for item in list_item:
            if item is not None:
                result.append(item)

    return result
