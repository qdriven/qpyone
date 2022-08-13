#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio

from fsdk.httpbin.api.httpmethod import HttpMethodService
from fluentqpy.clients.http.client import HttpClient, AsyncHttpClient


class TestHttpBinSdk:
    def setup(self):
        self.client = HttpClient()
        self.async_client = AsyncHttpClient()
        self.service = HttpMethodService(self.client)
        self.a_service = HttpMethodService(self.async_client)

    def test_get(self):
        resp = self.service.get()
        a_resp = asyncio.run(self.a_service.get())
        print(resp)
        print(a_resp)

    def test_put(self):
        resp = self.service.put()
        a_resp = asyncio.run(self.a_service.put())
        print(resp)
        print(a_resp)

    def test_post(self):
        resp = self.service.post()
        a_resp = asyncio.run(self.a_service.post())
        print(resp.dict())
        print(a_resp.dict())

    def test_delete(self):
        resp = self.service.delete()
        a_resp = asyncio.run(self.a_service.delete())
        print(resp.dict())
        print(a_resp.dict())
