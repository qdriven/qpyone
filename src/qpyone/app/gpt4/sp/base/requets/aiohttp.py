from __future__ import annotations

import aiohttp
from aiohttp import ClientSession, ClientResponse, ClientTimeout
from typing import AsyncGenerator, Any

from qpyone.app.gpt4.sp.base.constants import DEFAULT_HEADERS
from qpyone.app.gpt4.sp.base.utils import get_connector


class StreamResponse(ClientResponse):
    async def iter_lines(self) -> AsyncGenerator[bytes, None]:
        async for line in self.content:
            yield line.rstrip(b"\r\n")

    async def json(self) -> Any:
        return await super().json(content_type=None)


class StreamSession(ClientSession):
    def __init__(self, headers: dict = {}, timeout: int = None, proxies: dict = {},
                 impersonate=None, **kwargs):
        if impersonate:
            headers = {
                **DEFAULT_HEADERS,
                **headers
            }
        super().__init__(
            **kwargs,
            timeout=ClientTimeout(timeout) if timeout else None,
            response_class=StreamResponse,
            connector=get_connector(kwargs.get("connector"), proxies.get("https")),
            headers=headers, trust_env=True
        )
