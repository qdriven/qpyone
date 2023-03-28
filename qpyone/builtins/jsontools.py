"""
combine jmespath,jsonpath and dictor
- https://github.com/jmespath/jmespath.py
"""
from typing import Any
from typing import Dict
from typing import Union

import inspect
import json

import jmespath

from deepdiff import DeepDiff
from dotty_dict import dotty
from pydantic import BaseModel


def get(target_object: Any, path_exp: str) -> Any | None:
    """
    get value json/dict/class object
    """
    if isinstance(target_object, Dict):
        return jmespath.search(expression=path_exp, data=target_object)
    if isinstance(target_object, str):
        return jmespath.search(data=loads(target_object), expression=path_exp)
    if isinstance(target_object, BaseModel):
        return jmespath.search(data=target_object.dict(), expression=path_exp)
    raise NotImplementedError("not support type " + type(target_object))


def set_value(json_dict: Union[str, Dict], path_exp: str, to_value: Any) -> Dict:
    dot = dotty(json_dict)
    dot[path_exp] = to_value
    return dot.to_dict()


def differ(data_1: Union[str, dict], data_2: Union[str, dict]):
    if isinstance(data_1, str):
        v1 = loads(data_1)
        v2 = loads(data_2)
    else:
        v1 = data_1
        v2 = data_2

    return DeepDiff(v1, v2, verbose_level=2)


def loads(json_str: str, **kwargs):
    """
    load json str to json
    """
    return json.loads(json_str, **kwargs)


def load(file_path: str, **kwargs):
    """
    read json file to dict
    """
    with open(file_path) as f:
        return json.load(f, **kwargs)


def dumps(obj: dict | list, **kwargs) -> str:
    """
    dump string as json string
    """
    return json.dumps(obj=obj, **kwargs)
