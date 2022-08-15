#!/usr/bin/env python

import enum
from typing import Optional, Dict, Any,Awaitable, TypeVar, Union

from httpx import Response
from pydantic import BaseModel


from fluentqpy.misc import qweb

T = TypeVar("T")
SyncAsync = Union[T, Awaitable[T]]
ROOT_PATH = "/"

class ClientModel(BaseModel):
    """
    Base Model to separate dep
    """
    class Config:
        arbitrary_types_allowed =True

class HttpMethod(enum.Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTION = "OPTION"
    PATCH = "PATCH"


class HttpApiModel(ClientModel):
    base_url: Optional[str] = None
    method: str = HttpMethod.POST.value
    path: str = ROOT_PATH
    query: Optional[Dict[Any, Any]]
    body: Optional[Union[Dict[Any, Any], Any]]
    auth: Optional[Dict[str, Any]]
    headers: Optional[Dict[str, Any]]


class HttpRequest(HttpApiModel):
    name: Optional[str] = None
    path_params: Optional[Dict[str, Any]] = None
    query_params: Optional[Dict[str, Any]] = None
    req_url: Optional[str]

    def get_full_path(self, base_url=None):
        used_base_url = base_url if base_url else self.base_url
        self.req_url = fweb.normalize_url(used_base_url,
                                          fweb.replace_path_params(self.path, path_params=self.path_params))
        return self.req_url


class HttpResponse(ClientModel):
    raw_response: Response = None
    data: Any = None
    status_code: int = 200
    headers: Dict = None

    @staticmethod
    def from_raw_response(resp: Response):
        return HttpResponse(
            raw_response=resp,
            data=resp.json(),
            status_code=resp.status_code,
            headers=resp.headers
        )

class HttpLog(ClientModel):
    request: HttpRequest = None
    response: HttpResponse = None

    def resp_to_model(self, cls: type[BaseModel]):
        return cls.parse_obj(self.response.data)
