#!/usr/bin/env python
from types import TracebackType
from typing import Any

import dataclasses

from abc import abstractmethod

import httpx

from httpx import Response

from .errors import HttpRequestError
from .models import HttpLog
from .models import HttpRequest
from .models import HttpResponse
from .models import SyncAsync


@dataclasses.dataclass
class HttpClientOption:
    auth: dict | None = None
    timeout_ms = 50_000
    headers: dict | None = None
    additional: dict | None = None
    http2: bool = False


class BaseHttpClient:
    def __init__(
        self,
        client: httpx.Client | httpx.AsyncClient,
        options: dict[str, Any] | HttpClientOption | None = None,
        **kwargs,
    ):
        if options is None:
            options = HttpClientOption(**kwargs)
        elif isinstance(options, dict):
            options = HttpClientOption(**options)
        self.options = options
        self._clients: list[httpx.Client | httpx.AsyncClient] = []
        self.client = client
        self._default_headers = self._make_default_client_header(options)

    @staticmethod
    def _make_default_client_header(
        options: dict[str, Any] | HttpClientOption | None
    ) -> httpx.Headers:
        headers = httpx.Headers()
        if options:
            if options.auth:
                headers.update(options.auth)
            if options.headers:
                headers.update(options.headers)
        return headers

    @property
    def client(self) -> httpx.Client | httpx.AsyncClient:
        return self._clients[-1]

    @client.setter
    def client(self, client: httpx.Client | httpx.AsyncClient):
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        self._clients.append(client)

    def _pre_request(self, req: HttpRequest, **kwargs) -> HttpRequest:
        if req is None:
            if kwargs is not None:
                req = HttpRequest(**kwargs)
            else:
                raise ValueError("lack of api request parameters")
        send_header = self._default_headers.copy()
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
        self.logger.info(f"=> {req.query} -- {req.body}")
        return self.client.build_request(
            req.method,
            req.req_url,
            params=req.query,
            json=req.body,
            headers=req.headers,
        )

    def _parse_http_log(self, req: HttpRequest, resp: Response) -> HttpLog:
        return HttpLog(request=req, response=HttpResponse.from_raw_response(resp))

    @abstractmethod
    def request(self, req: HttpRequest = None, **kwargs) -> SyncAsync[Any]:
        pass


class HttpClient(BaseHttpClient):
    """Sync Http Client"""

    client: httpx.Client

    def __init__(
        self,
        options: dict[Any, Any] | HttpClientOption | None = None,
        client: httpx.Client | None = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.Client()
        super().__init__(client, options, **kwargs)

    def __enter__(self) -> "HttpClient":
        self.client = httpx.Client()
        self.client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
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
    """Asynchronous clients for Notion's API."""

    client: httpx.AsyncClient

    def __init__(
        self,
        options: dict[str, Any] | HttpClientOption | None = None,
        client: httpx.AsyncClient | None = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.AsyncClient()
        super().__init__(client, options, **kwargs)

    async def __aenter__(self) -> "AsyncHttpClient":
        self.client = httpx.AsyncClient()
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
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
