from __future__ import annotations

from uuid import uuid4

from qpyone.app.gpt4.sp.base.base_provider import BaseProvider
from qpyone.app.gpt4.sp.base.request import get_session_from_browser
from qpyone.app.gpt4.sp.base.schemas import Messages, CompletionResult


class Bestim(BaseProvider):
    url = "https://chatgpt.bestim.org"
    supports_gpt_35_turbo = True
    supports_message_history = True
    working = False
    supports_stream = True

    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool,
        proxy: str = None,
        **kwargs
    ) -> CompletionResult:
        session = get_session_from_browser(cls.url, proxy=proxy)
        headers = {
            'Accept': 'application/json, text/event-stream',
        }
        data = {
            "messagesHistory": [{
                "id": str(uuid4()),
                "content": m["content"],
                "from": "you" if m["role"] == "user" else "bot"
            } for m in messages],
            "type": "chat",
        }
        response = session.post(
            url="https://chatgpt.bestim.org/chat/send2/",
            json=data,
            headers=headers,
            stream=True
        )
        response.raise_for_status()
        for line in response.iter_lines():
            if not line.startswith(b"event: trylimit"):
                yield line.decode().removeprefix("data: ")
