#!/usr/bin/env python
from typing import Any
from typing import Dict
from typing import List
from typing import Type

from pydantic import BaseModel


def sql_result_to_model(result, model_type: type[BaseModel]) -> list[Any]:
    all_list = []
    for row in result:
        result_dict = {}
        for key in result.keys():
            result_dict[key] = str(row[key])
        all_list.append(model_type(**result_dict))
    return all_list


def sql_result_to_dict(result) -> list[dict]:
    all_list = []
    for row in result:
        result_dict = {}
        for key in result.keys():
            result_dict[key] = str(row[key])
        all_list.append(result_dict)
    return all_list
