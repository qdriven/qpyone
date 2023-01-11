#!/usr/bin/env python

import pytest

from qpyone.clients.http.client import AsyncHttpClient
from qpyone.clients.http.client import HttpClient

from tests.clients.demo.httpmethod import HttpMethodTestService


# @pytest.mark.skip
class TestHttpBinSdk:
    def setup(self):
        self.client = HttpClient()
        self.async_client = AsyncHttpClient()
        self.service = HttpMethodTestService(self.client)
        self.a_service = HttpMethodTestService(self.async_client)

    def test_get(self):
        resp = self.service.get()
        print(resp)
        resp = self.service.delete()
        print(resp)
        resp = self.service.put()
        print(resp)
        resp = self.service.post()
        print(resp)
