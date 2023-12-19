#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any

from qpybase import BaseDataModel


class ClientRequest(BaseDataModel):
    type: str = "HTTP"
    request: Any
    context: Any


class ClientResponse(BaseDataModel):
    type: str
    response: Any
    context: Any
