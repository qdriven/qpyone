#!/usr/bin/env python
from typing import Optional
from typing import Tuple

from collections.abc import Iterable
from dataclasses import dataclass


class ResponseDataNotFound(Exception):
    pass


@dataclass(frozen=True)
class RequestMetaData:
    url: str
    method: str
    status: int
    body: str


@dataclass(frozen=True)
class HttpResponse:
    status: int
    headers: Iterable[tuple[str, str]]
    body: str | None
