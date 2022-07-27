#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Any, Dict
from urllib.parse import urlparse


def replace_path_params(path: str, path_params: Dict[str, Any] = None) -> str:
    parsed = urlparse(path)
    if parsed.netloc:
        raise ValueError("host/domain location is included, please remove it")
    path = parsed.path
    if path_params:
        for key in path_params:
            path = path.replace("{" + key + "}", str(path_params[key]))
    return path


def normalize_url(base_url: str, path: str) -> str:
    if (base_url.endswith("/") and path.startswith("/")) or (not base_url.endswith("/") and not path.startswith("/")):
        return "/".join([base_url, path]).replace("///", "/")
    return base_url + path
