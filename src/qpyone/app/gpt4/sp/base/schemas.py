from __future__ import annotations

import sys
from typing import Any, AsyncGenerator, Generator, NewType, Tuple, Union, List, Dict, \
    Type, IO, Optional



try:
    from PIL.Image import Image
except ImportError:
    from typing import Type as Image


if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

SHA256 = NewType('sha_256_hash', str)
CompletionResult = Generator[str, None, None]
AsyncCompletionResult = AsyncGenerator[str, None]
Messages = List[Dict[str, str]]
Cookies = Dict[str, str]
ImageType = Union[str, bytes, IO, Image, None]




#
# # GPT-3.5 too, but all providers supports long requests and responses
# gpt_35_long = AIModelInfo(
#     name='gpt-3.5-turbo',
#     base_provider='openai',
#     best_provider=RetryProvider([
#         FreeGpt, You,
#         GeekGpt, FakeGpt,
#         Chatgpt4Online,
#         ChatgptDemoAi,
#         ChatgptNext,
#         ChatgptDemo,
#         Gpt6,
#     ])
# )
#
# # GPT-3.5 / GPT-4
# gpt_35_turbo = AIModelInfo(
#     name='gpt-3.5-turbo',
#     base_provider='openai',
#     best_provider=RetryProvider([
#         GptGo, You,
#         GptForLove, ChatBase,
#         Chatgpt4Online,
#     ])
# )
#
# gpt_4 = AIModelInfo(
#     name='gpt-4',
#     base_provider='openai',
#     best_provider=RetryProvider([
#         Bing, Phind, Liaobots,
#     ])
# )
#
# gpt_4_turbo = AIModelInfo(
#     name='gpt-4-turbo',
#     base_provider='openai',
#     best_provider=Bing
# )
#
# llama2_7b = AIModelInfo(
#     name="meta-llama/Llama-2-7b-chat-hf",
#     base_provider='huggingface',
#     best_provider=RetryProvider([Llama2, DeepInfra])
# )
#
# llama2_13b = AIModelInfo(
#     name="meta-llama/Llama-2-13b-chat-hf",
#     base_provider='huggingface',
#     best_provider=RetryProvider([Llama2, DeepInfra])
# )
#
# llama2_70b = AIModelInfo(
#     name="meta-llama/Llama-2-70b-chat-hf",
#     base_provider="huggingface",
#     best_provider=RetryProvider([Llama2, DeepInfra, HuggingChat, PerplexityLabs])
# )
#
# codellama_34b_instruct = AIModelInfo(
#     name="codellama/CodeLlama-34b-Instruct-hf",
#     base_provider="huggingface",
#     best_provider=RetryProvider([HuggingChat, PerplexityLabs, DeepInfra])
# )
#
# # Mistral
# mixtral_8x7b = AIModelInfo(
#     name="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     base_provider="huggingface",
#     best_provider=RetryProvider([DeepInfra, HuggingChat, PerplexityLabs])
# )
#
# mistral_7b = AIModelInfo(
#     name="mistralai/Mistral-7B-Instruct-v0.1",
#     base_provider="huggingface",
#     best_provider=RetryProvider([DeepInfra, HuggingChat, PerplexityLabs])
# )
#
# # Misc models
# dolphin_mixtral_8x7b = AIModelInfo(
#     name="cognitivecomputations/dolphin-2.6-mixtral-8x7b",
#     base_provider="huggingface",
#     best_provider=DeepInfra
# )
#
# lzlv_70b = AIModelInfo(
#     name="lizpreciatior/lzlv_70b_fp16_hf",
#     base_provider="huggingface",
#     best_provider=DeepInfra
# )
#
# airoboros_70b = AIModelInfo(
#     name="deepinfra/airoboros-70b",
#     base_provider="huggingface",
#     best_provider=DeepInfra
# )
#
# airoboros_l2_70b = AIModelInfo(
#     name="jondurbin/airoboros-l2-70b-gpt4-1.4.1",
#     base_provider="huggingface",
#     best_provider=DeepInfra
# )
#
# openchat_35 = Model(
#     name="openchat/openchat_3.5",
#     base_provider="huggingface",
#     best_provider=RetryProvider([DeepInfra, HuggingChat])
# )
#
# # Bard
# bard = palm = Model(
#     name='palm',
#     base_provider='google',
#     best_provider=Bard
# )
#
# claude_v2 = Model(
#     name='claude-v2',
#     base_provider='anthropic',
#     best_provider=RetryProvider([FreeChatgpt, Vercel])
# )
#
# gpt_35_turbo_16k = Model(
#     name='gpt-3.5-turbo-16k',
#     base_provider='openai',
#     best_provider=gpt_35_long.best_provider
# )
#
# gpt_35_turbo_16k_0613 = Model(
#     name='gpt-3.5-turbo-16k-0613',
#     base_provider='openai',
#     best_provider=gpt_35_long.best_provider
# )
#
# gpt_35_turbo_0613 = Model(
#     name='gpt-3.5-turbo-0613',
#     base_provider='openai',
#     best_provider=gpt_35_turbo.best_provider
# )
#
# gpt_4_0613 = Model(
#     name='gpt-4-0613',
#     base_provider='openai',
#     best_provider=gpt_4.best_provider
# )
#
# gpt_4_32k = Model(
#     name='gpt-4-32k',
#     base_provider='openai',
#     best_provider=gpt_4.best_provider
# )
#
# gpt_4_32k_0613 = Model(
#     name='gpt-4-32k-0613',
#     base_provider='openai',
#     best_provider=gpt_4.best_provider
# )
#
# gemini_pro = Model(
#     name='gemini-pro',
#     base_provider='google',
#     best_provider=RetryProvider([FreeChatgpt, GeminiProChat])
# )
#
# pi = Model(
#     name='pi',
#     base_provider='inflection',
#     best_provider=Pi
# )
#
#
# class ModelUtils:
#     """
#     Utility class for mapping string identifiers to Model instances.
#
#     Attributes:
#         convert (dict[str, Model]): Dictionary mapping model string identifiers to Model instances.
#     """
#     convert: dict[str, Model] = {
#         # gpt-3.5
#         'gpt-3.5-turbo': gpt_35_turbo,
#         'gpt-3.5-turbo-0613': gpt_35_turbo_0613,
#         'gpt-3.5-turbo-16k': gpt_35_turbo_16k,
#         'gpt-3.5-turbo-16k-0613': gpt_35_turbo_16k_0613,
#
#         'gpt-3.5-long': gpt_35_long,
#
#         # gpt-4
#         'gpt-4': gpt_4,
#         'gpt-4-0613': gpt_4_0613,
#         'gpt-4-32k': gpt_4_32k,
#         'gpt-4-32k-0613': gpt_4_32k_0613,
#         'gpt-4-turbo': gpt_4_turbo,
#
#         # Llama 2
#         'llama2-7b': llama2_7b,
#         'llama2-13b': llama2_13b,
#         'llama2-70b': llama2_70b,
#         'codellama-34b-instruct': codellama_34b_instruct,
#
#         'mixtral-8x7b': mixtral_8x7b,
#         'mistral-7b': mistral_7b,
#         'dolphin-mixtral-8x7b': dolphin_mixtral_8x7b,
#         'lzlv-70b': lzlv_70b,
#         'airoboros-70b': airoboros_70b,
#         'airoboros-l2-70b': airoboros_l2_70b,
#         'openchat_3.5': openchat_35,
#         'gemini-pro': gemini_pro,
#         'bard': bard,
#         'claude-v2': claude_v2,
#         'pi': pi
#     }
#
#
# _all_models = list(ModelUtils.convert.keys())
#
#
# class ProviderDetail(BaseDataModel):
#     name: str
#     url: str
#     model_info: AIModelInfo
#
#
__all__ = [
    'Any',
    'AsyncGenerator',
    'Generator',
    'Tuple',
    'Union',
    'List',
    'Dict',
    'Type',
    'IO',
    'Optional',
    'TypedDict',
    'SHA256',
    'CompletionResult',
    'AsyncCompletionResult',
    'Messages',
    'Cookies',
    'Image',
    'ImageType'
]
