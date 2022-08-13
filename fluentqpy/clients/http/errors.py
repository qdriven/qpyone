#!/usr/bin/env python
# -*- coding:utf-8 -*-


class HttpRequestError(Exception):
    code = "http_request_error"
    ex: Exception

    def __init__(self, ex: Exception, message: str = "Http Request error") -> None:
        super().__init__(message)
        self.ex = ex

