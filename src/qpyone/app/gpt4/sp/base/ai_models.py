from qpystructs import BaseDataModel

from qpyone.app.gpt4.providers.base.retry_provider import RetryProvider


class AIModelInfo(BaseDataModel):
    name: str
    base_provider: str
    best_provider: str


default = AIModelInfo(
    name="",
    base_provider="",
    best_provider=RetryProvider([
        # Bing,
        # ChatgptAi, GptGo, GeekGpt,
        # You,
        # Chatgpt4Online
    ])
)
