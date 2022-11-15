#!/usr/bin/env python
from typing import List

from qpyone.core.models import QBaseModel


class DbConfig(QBaseModel):
    url: str | None = None
    pool_size: int | None = None


class FieldMeta(QBaseModel):
    field_name: str
    field_type: str
    code_type: str = ""
    code_value: str = ""


class TableMeta(QBaseModel):
    table_name: str
    fields: list[FieldMeta]
