#!/usr/bin/env python

from qpyone.core.models import QBaseModel


class DbConfig(QBaseModel):
    url: str | None = None
    pool_size: int | None = None
