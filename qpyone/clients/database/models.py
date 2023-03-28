#!/usr/bin/env python
from qpyone.base import BaseDataModel


class DbConfig(BaseDataModel):
    url: str | None = None
    pool_size: int | None = None


class FieldMeta(BaseDataModel):
    field_name: str
    field_type: str
    code_type: str = ""
    code_value: str = ""


class TableMeta(BaseDataModel):
    table_name: str
    fields: list[FieldMeta]
