from typing import TypeVar
from typing import Union

import re

import inflection
import pydantic

from pydantic import BaseModel
from pydantic.generics import GenericModel


T = TypeVar("T")  # Declare type variable


def to_camel(s: str) -> str:
    s = re.sub("_(url)$", lambda m: f"_{m.group(1).upper()}", s)
    return inflection.camelize(s, uppercase_first_letter=False)


class CamelModel(BaseModel):
    def __init__(self, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        super().__init__(**kwargs)

    class Config:
        arbitrary_types_allowed = True
        alias_generator = to_camel
        allow_population_by_field_name = True
        # Populate enum values with their value, rather than the raw enum. Important to serialise model.dict()
        use_enum_values = True

    def to_json(self, by_alias=True):
        return self.json(by_alias=by_alias, exclude_none=True)

    def to_dict(self, by_alias=True):
        return self.dict(by_alias=by_alias, exclude_none=True)


class GenericDataModel(CamelModel, GenericModel):
    pass


class BaseDataModel(GenericDataModel):
    pass


def parse_as(json_str: str, to_type: Union[GenericDataModel, BaseDataModel, BaseModel]):
    return pydantic.parse_raw_as(to_type)


def to_json(obj: Union[GenericDataModel, BaseDataModel, BaseModel]):
    if isinstance(obj, GenericDataModel) or isinstance(obj, BaseDataModel):
        return obj.to_json()
    else:
        return obj.json(by_alias=True, exclude_none=True)
