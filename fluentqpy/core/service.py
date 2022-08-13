#!/usr/bin/env python
# -*- coding:utf-8 -*-

import functools
from typing import Union, Any, Dict

from pydantic import BaseModel

from fluentqpy.clients.http.client import BaseHttpClient
from fluentqpy.clients.http.models import HttpRequest, HttpLog
from fluentqpy.builtins.structstools import pick_value


class BaseRpcService:

    def __init__(self, invoker: Union[BaseHttpClient, Any] = None, **kwargs):
        self.invoker = invoker
        base_url_input = pick_value(kwargs, "base_url")
        if base_url_input:
            self.base_url = base_url_input
        self.options = kwargs

    def _make_request_model(self, **kwargs) -> HttpRequest:
        request = HttpRequest(**kwargs)
        if request.base_url is None:
            request.base_url = self.base_url
        return request

    def request(self, name: str, path: str, body: Union[Dict, BaseModel] = None, **kwargs) -> HttpLog:
        req = self._make_request_model(
            name=name,
            path=path,
            body=body.dict() if body else {},
            **kwargs
        )
        return self.invoker.request(req)

    def _partial_ncp_request(self, name: str, path: str):
        return functools.partial(self.request, name, path)

    @classmethod
    def create(cls, invoker: BaseHttpClient = None, **kwargs):
        return cls(invoker, **kwargs)
