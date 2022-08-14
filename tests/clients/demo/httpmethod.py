#!/usr/bin/env python
# -*- coding:utf-8 -*-

from spell.clients.http.models import HttpMethod
from spell.clients.service import BaseRpcService


class HttpMethodTestService(BaseRpcService):
    base_url = "http://httpbin.org/"

    def get(self):
        req = self._make_request(method="get", path="/get")
        return self.invoker.request(
            req
        )

    def delete(self):
        req = self._make_request(method="delete", path="/delete")
        return self.invoker.request(
            req
        )

    def put(self):
        req = self._make_request(method="put", path="/put")
        return self.invoker.request(
            req
        )

    def post(self):
        req = self._make_request(method=HttpMethod.POST.value, path="/post")
        return self.invoker.request(
            req
        )
