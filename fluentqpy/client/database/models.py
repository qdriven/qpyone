#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional

from fluentqpy.builtins.models import FBaseModel


class DbConfig(FBaseModel):
    url: Optional[str]= None
    pool_size: Optional[int]=None
