#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any


class ClientRequest(BaseDataModel):
    type: str = "HTTP"
    request: Any
    context: Any


class ClientResponse(BaseDataModel):
    type: str
    response: Any
    context: Any
