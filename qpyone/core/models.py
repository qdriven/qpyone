#!/usr/bin/env python
from pydantic import BaseModel


class BaseDataModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        # alias_generator = to_camel
        allow_population_by_field_name = True
        use_enum_values = True

    def to_json(self):
        return self.json(by_alias=True, exclude_none=True)

    def to_dict(self):
        return self.dict(by_alias=True, exclude_none=True)
