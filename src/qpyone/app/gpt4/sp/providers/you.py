from __future__ import annotations

import json

from qpyone.app.gpt4.sp.base.base_async_provider import AsyncGeneratorProvider
from qpyone.app.gpt4.sp.base.prompts.base import format_prompt
from qpyone.app.gpt4.sp.base.requets.aiohttp import StreamSession
from qpyone.app.gpt4.sp.base.schemas import Messages, AsyncGenerator


class You(AsyncGeneratorProvider):
    url = "https://you.com"
    working = True
    supports_gpt_35_turbo = True


    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        timeout: int = 120,
        **kwargs,
    ) -> AsyncGenerator:
        async with StreamSession(proxies={"https": proxy}, impersonate="chrome107",
                                 timeout=timeout) as session:
            headers = {
                "Accept": "text/event-stream",
                "Referer": f"{cls.url}/search?fromSearchBar=true&tbm=youchat",
            }
            data = {"q": format_prompt(messages), "domain": "youchat", "chat": ""}
            async with session.get(
                f"{cls.url}/api/streamingSearch",
                params=data,
                headers=headers
            ) as response:
                response.raise_for_status()
                start = b'data: {"youChatToken": '
                async for line in response.iter_lines():
                    if line.startswith(start):
                        yield json.loads(line[len(start):-1])
