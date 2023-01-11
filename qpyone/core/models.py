#!/usr/bin/env python
from pydantic import BaseModel


class BaseDataModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        # alias_generator = to_camel
        allow_population_by_field_name = True
        use_enum_values = True

    def to_json(self, by_alias=True):
        return self.json(by_alias=by_alias, exclude_none=True)

    def to_dict(self, by_alias=True):
        return self.dict(by_alias=by_alias, exclude_none=True)
