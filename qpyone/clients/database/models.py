#!/usr/bin/env python
from typing import Optional

from qpyone.builtins.models import FBaseModel


class DbConfig(FBaseModel):
    url: str | None = None
    pool_size: int | None = None
