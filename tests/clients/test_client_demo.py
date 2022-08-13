#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio

from fluentqpy.clients.http.client import HttpClient, AsyncHttpClient
from tests.clients.demo.httpmethod import HttpMethodTestService
from tests.clients.demo.httpmethod_partial import PHttpMethodTestService


class TestHttpBinSdk:
    def setup(self):
        self.client = HttpClient()
        self.async_client = AsyncHttpClient()
        self.service = HttpMethodTestService(self.client)
        self.a_service = HttpMethodTestService(self.async_client)
        self.p_service = PHttpMethodTestService(self.client)

    def test_get(self):
        resp = self.service.get()
        a_resp = asyncio.run(self.a_service.get())
        print(resp)
        print(a_resp)
        p_resp = self.p_service.request("GET")
        print(p_resp)

    def test_put(self):
        resp = self.service.put()
        a_resp = asyncio.run(self.a_service.put())
        print(resp)
        print(a_resp)
        p_resp = self.p_service.request("PUT")
        print(p_resp)

    def test_post(self):
        resp = self.service.post()
        a_resp = asyncio.run(self.a_service.post())
        print(resp.dict())
        print(a_resp.dict())
        p_resp = self.p_service.request("POST")
        print(p_resp)

    def test_delete(self):
        resp = self.service.delete()
        a_resp = asyncio.run(self.a_service.delete())
        print(resp.dict())
        print(a_resp.dict())
        p_resp = self.p_service.request("DELETE")
        print(p_resp)
