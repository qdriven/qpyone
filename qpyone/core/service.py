#!/usr/bin/env python

from typing import Any

import functools

from pydantic import BaseModel
from qpyone.builtins.dicttools import pick_value
from qpyone.clients.http.client import BaseHttpClient
from qpyone.clients.http.models import HttpLog
from qpyone.clients.http.models import HttpRequest


class BaseRpcService:
    def __init__(self, invoker: BaseHttpClient | Any = None, **kwargs):
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

    def request(
        self, name: str, path: str, body: dict | BaseModel = None, **kwargs
    ) -> HttpLog:
        req = self._make_request_model(
            name=name, path=path, body=body.dict() if body else {}, **kwargs
        )
        return self.invoker.request(req)

    def _partial_ncp_request(self, name: str, path: str):
        return functools.partial(self.request, name, path)

    @classmethod
    def create(cls, invoker: BaseHttpClient = None, **kwargs):
        return cls(invoker, **kwargs)
