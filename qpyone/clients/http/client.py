#!/usr/bin/env python
# -*- coding:utf-8 -*-
from types import TracebackType
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import Union

from abc import abstractmethod

import httpx

from httpx import Response
from qpybase import BaseDataModel
from qpyone.clients.http.errors import HttpRequestError
from qpyone.clients.http.models import HttpLog
from qpyone.clients.http.models import HttpRequest
from qpyone.clients.http.models import HttpResponse
from qpyone.clients.http.models import SyncAsync
from qpyone.core import qpy_logger


class HttpClientOption(BaseDataModel):
    auth: Optional[Dict] = None
    timeout_ms = 50_000
    headers: Optional[Dict] = None
    additional: Optional[Dict] = None
    ## Default to False
    http2: Optional[bool] = False


class BaseHttpClient:
    def __init__(
        self,
        client: Union[httpx.Client, httpx.AsyncClient],
        options: Optional[Union[Dict[str, Any], HttpClientOption]] = None,
        **kwargs,
    ):
        if options is None:
            options = HttpClientOption(**kwargs)
        elif isinstance(options, dict):
            options = HttpClientOption(**options)
        self.options = options
        self._clients: List[Union[httpx.Client, httpx.AsyncClient]] = []
        self.client = client
        self._default_headers = self._make_default_client_header(options)
        self.logger = qpy_logger
        self._auth = {}

    @staticmethod
    def _make_default_client_header(
        options: Optional[Union[Dict[str, Any], HttpClientOption]]
    ) -> httpx.Headers:
        headers = httpx.Headers()
        if options:
            if options.auth:
                headers.update(options.auth)
            if options.headers:
                headers.update(options.headers)
        return headers

    def auth(self, key, value):
        self._auth[key] = value
        return self

    @property
    def client(self) -> Union[httpx.Client, httpx.AsyncClient]:
        return self._clients[-1]

    @client.setter
    def client(self, client: Union[httpx.Client, httpx.AsyncClient]):
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        self._clients.append(client)

    def _pre_request(self, req: HttpRequest, **kwargs) -> HttpRequest:
        if req is None:
            if kwargs is not None:
                req = HttpRequest(**kwargs)
            else:
                raise ValueError("lack of api request parameters")
        send_header = self._default_headers.copy()
        send_header.update(self._auth)
        if req.headers:
            send_header.update(req.headers)
        if req.auth:
            send_header.update(req.auth)
        if req.base_url:
            req.req_url = req.get_full_path(req.base_url)
        req.headers = send_header
        return req

    def _build_request(self, req: HttpRequest):
        self.logger.info(f"{req.method} {req.req_url}")
        self.logger.info(f"request-body: {req.body}")
        return self.client.build_request(
            req.method,
            req.req_url,
            params=req.query,
            json=req.body,
            headers=req.headers,
        )

    def _parse_http_log(self, req: HttpRequest, resp: Response) -> HttpLog:
        try:
            return HttpLog(request=req, response=HttpResponse.from_raw_response(resp))
        except Exception as e:
            self.logger.error(e)
            return HttpLog(request=req, response=HttpResponse(raw_response=resp))

    @abstractmethod
    def request(self, req: HttpRequest = None, **kwargs) -> SyncAsync[Any]:
        pass


class HttpClient(BaseHttpClient):
    """Sync Http Client"""

    client: httpx.Client

    def __init__(
        self,
        options: Optional[Union[Dict[Any, Any], HttpClientOption]] = None,
        client: Optional[httpx.Client] = None,
        **kwargs: Any,
    ) -> None:
        if options is None:
            options = HttpClientOption()
        if client is None:
            if options.http2:
                client = httpx.Client(http2=options.http2, http1=False, verify=False)
            else:
                client = httpx.Client(verify=False)
        super().__init__(client, options, **kwargs)

    def __enter__(self) -> "HttpClient":
        self.client = httpx.Client()
        self.client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        self.client.__exit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    def close(self) -> None:
        self.client.close()

    def request(self, req: HttpRequest = None, **kwargs) -> Any:
        req = self._pre_request(req, **kwargs)
        request = self._build_request(req)
        try:
            response = self.client.send(request)
        except Exception as e:
            raise HttpRequestError(e)
        return self._parse_http_log(req, response)


class AsyncHttpClient(BaseHttpClient):
    """Asynchronous client for Notion's API."""

    client: httpx.AsyncClient

    def __init__(
        self,
        options: Optional[Union[Dict[str, Any], HttpClientOption]] = None,
        client: Optional[httpx.AsyncClient] = None,
        **kwargs: Any,
    ) -> None:
        if options is None:
            options = HttpClientOption()
        if client is None:
            if options.http2:
                client = httpx.AsyncClient(
                    http2=options.http2, http1=False, verify=False
                )
            else:
                client = httpx.AsyncClient(verify=False)
        super().__init__(client, options, **kwargs)

    async def __aenter__(self) -> "AsyncHttpClient":
        self.client = httpx.AsyncClient()
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        await self.client.__aexit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    async def aclose(self) -> None:
        await self.client.aclose()

    async def request(self, req: HttpRequest = None, **kwargs) -> Any:
        req = self._pre_request(req, **kwargs)
        request = self._build_request(req)
        try:
            response = await self.client.send(request)
        except Exception as e:
            raise HttpRequestError(e)
        return self._parse_http_log(req, response)
