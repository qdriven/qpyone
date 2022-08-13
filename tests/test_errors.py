#!/usr/bin/env python
# -*- coding:utf-8 -*-
from fluentqpy.clients.http.errors import HttpRequestError


def test_http_request_error():

    ex = HttpRequestError(Exception("raw-msg"))
    assert ex.ex is not None
