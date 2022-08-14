#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Union, Any

from spell.clients.http.client import BaseHttpClient
from spell.clients.http.models import HttpRequest
from spell.clients.service import BaseRpcService


class PHttpMethodTestService(BaseRpcService):
    base_url = "http://httpbin.org/"
    API_MAP = {
        "GET": HttpRequest(api_name="get api", path="/get", method="get", base_url=base_url),
        "DELETE": HttpRequest(api_name="delete api", path="/delete", method="delete", base_url=base_url),
        "PUT": HttpRequest(api_name="put api", path="/put", method="put", base_url=base_url),
        "POST": HttpRequest(api_name="POST api", path="/post", method="post", base_url=base_url)

    }

    def __init__(self, invoker: Union[BaseHttpClient, Any], **kwargs):
        super(PHttpMethodTestService, self).__init__(invoker, **kwargs)
        self.get = self._make_partial_request_func(self.API_MAP["GET"])
        self.delete = self._make_partial_request_func(self.API_MAP["DELETE"])
        self.put = self._make_partial_request_func(self.API_MAP["PUT"])
        self.post = self._make_partial_request_func(self.API_MAP["POST"])

    def request(self, api_name, **kwargs):
        return self._make_partial_request_func(self.API_MAP[api_name])(**kwargs)
