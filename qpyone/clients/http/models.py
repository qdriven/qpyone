#!/usr/bin/env python

from typing import Any
from typing import Dict
from typing import Optional
from typing import TypeVar
from typing import Union

import enum

from collections.abc import Awaitable

from httpx import Response
from pydantic import BaseModel


T = TypeVar("T")
SyncAsync = Union[T, Awaitable[T]]
ROOT_PATH = "/"


class ClientModel(BaseModel):
    """
    Base Model to separate dep
    """

    class Config:
        arbitrary_types_allowed = True


class HttpMethod(enum.Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTION = "OPTION"
    PATCH = "PATCH"


class HttpApiModel(ClientModel):
    base_url: str | None = None
    method: str = HttpMethod.POST.value
    path: str = ROOT_PATH
    query: dict[Any, Any] | None
    body: dict[Any, Any] | Any | None
    auth: dict[str, Any] | None
    headers: dict[str, Any] | None


class HttpRequest(HttpApiModel):
    name: str | None = None
    path_params: dict[str, Any] | None = None
    query_params: dict[str, Any] | None = None
    req_url: str | None

    def get_full_path(self, base_url=None):
        used_base_url = base_url if base_url else self.base_url
        self.req_url = fweb.normalize_url(
            used_base_url,
            fweb.replace_path_params(self.path, path_params=self.path_params),
        )
        return self.req_url


class HttpResponse(ClientModel):
    raw_response: Response = None
    data: Any = None
    status_code: int = 200
    headers: dict = None

    @staticmethod
    def from_raw_response(resp: Response):
        return HttpResponse(
            raw_response=resp,
            data=resp.json(),
            status_code=resp.status_code,
            headers=resp.headers,
        )


class HttpLog(ClientModel):
    request: HttpRequest = None
    response: HttpResponse = None

    def resp_to_model(self, cls: type[BaseModel]):
        return cls.parse_obj(self.response.data)
