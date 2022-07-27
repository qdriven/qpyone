#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Any, Dict, Union


def pick_by_keys(base: Dict[Any, Any], *keys: str) -> Dict[Any, Any]:
    result = {}
    for key in keys:
        if key in base and base[key] is not None:
            result[key] = base[key]
    return result


def pick_values(base: Dict[Any, Any], *keys: str) -> list[Any]:
    result = []
    for key in keys:
        if key in base and base[key] is not None:
            result.append(base[key])
    return result


def pick_value(base: Dict[Any, Any], *keys: str) -> Union[Any, None]:
    for key in keys:
        if key in base and base[key] is not None:
            return base[key]
    return None
