#!/usr/bin/env python
from typing import Optional

import json

from collections.abc import Iterable
from dataclasses import dataclass

from mitmproxy.http import HTTPFlow
from qpyone.clients import DbClient
from qpyone.clients import DbConfig
from qpyone.core import configs
from sqlmodel import Field
from sqlmodel import SQLModel


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


class ApiMonitorRecord(SQLModel, table=True):
    __tablename__ = "api_monitor_record"
    # __table_args__ = {"schema": "public"}
    id: int | None = Field(default=None, primary_key=True)
    body: str | None = None
    headers: str | None = None
    method: str | None = None
    request_url: str | None = None
    service: str | None = None


db_client = DbClient(DbConfig(url=configs.db.url))


def save_http_flow(flow: HTTPFlow):
    header_dict = {}
    for key, value in flow.request.headers.items():
        header_dict[key] = value
    service = flow.request.path
    record = ApiMonitorRecord(
        method=flow.request.method,
        headers=json.dumps(header_dict),
        request_url=flow.request.url,
        service=service,
        body=flow.request.content,
    )
    db_client.save(record)
