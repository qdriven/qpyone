#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fluentqpy.builtins.dicttools import *
from fluentqpy.misc.fweb import *


def test_pick_by_keys():
    result = pick_by_keys({"test": "value", "k1": "v2"}, "test")
    assert result == {"test": "value"}


def test_pick_by_keys_none():
    result = pick_by_keys({"test": "value", "k1": "v2"}, "test1")
    assert result == {}


def test_pick_values():
    result = pick_values({"test": "value", "k1": "v2"}, "test1")
    assert result == []


def test_pick_value():
    result = pick_value({"test": "value", "k1": "v2"}, "test1")
    assert result is None


def test_web_replace_url():
    result = replace_path_params("/todo/{todo}/task/{taskId}?q=t&&v=t",
                                 {"todo": 123, "taskId": "new"})
    assert result == "/todo/123/task/new"


def test_web_replace_url():
    result = replace_path_params("todo/{todo}/task/{taskId}?q=t&&v=t", )
    assert result == "todo/{todo}/task/{taskId}"


def test_replace_double_slash():
    assert "//test//t".replace("//", "/") == "/test/t"


def test_normalize_url():
    result = normalize_url("http://httpbin.org/", "/get")
    assert result == "http://httpbin.org/get"


def test_normalize_url_new():
    result = normalize_url("http://httpbin.org", "/get")
    assert result == "http://httpbin.org/get"
