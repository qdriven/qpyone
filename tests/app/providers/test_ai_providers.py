from typing import Type

from qpyone.app.gpt4.sp.providers.HuggingChat import HuggingChat
from qpyone.app.gpt4.sp.providers.Koala import Koala
from qpyone.app.gpt4.sp.providers.Liaobots import Liaobots
from qpyone.app.gpt4.sp.providers.Llama2 import Llama2
from qpyone.app.gpt4.sp.providers.aura import Aura
from qpyone.app.gpt4.sp.providers.chatbase import ChatBase
from qpyone.app.gpt4.sp.providers.chatgptfree import ChatgptFree
from qpyone.app.gpt4.sp.disabled.ai_ask import AiAsk
from qpyone.app.gpt4.sp.disabled.ai_chatonline import AiChatOnline
from qpyone.app.gpt4.sp.disabled.chat_anywhere import ChatAnywhere

from qpyone.app.gpt4.sp.providers.you import You


def test_create_async_generator():
    fluetnai = AiAsk()
    result = fluetnai.create_completion(model="ignored", messages=[
        {"role": "user", "content": "如何使用python"}])
    for item in result:
        print(item)


def test_ai_chatonline():
    fluetnai = AiChatOnline()
    result = fluetnai.create_completion(model="ignored", messages=[
        {"role": "user", "content": "如何使用python"}])
    for item in result:
        print(item)


## 可以使用
def test_chatgpt_fee():
    fluetnai = ChatgptFree()
    result = fluetnai.create_completion(model="ignored", messages=[
        {"role": "user", "content": "如何使用python"}])
    for item in result:
        print(item)


def test_chat_anywhere():
    fluetnai = ChatAnywhere()
    result = fluetnai.create_completion(model="ignored", messages=[
        {"role": "user", "content": "如何使用python"}])
    for item in result:
        print(item)


def call_chatlike(clazz:Type,model="ignored",**kwargs):
    fluetnai = clazz()
    result = fluetnai.create_completion(model=model, messages=[
        {"role": "user", "content": "如何使用python"}],**kwargs)
    print(result)
    for item in result:
        print(item)
def test_chatbase():
    call_chatlike(ChatBase)

def test_aura():
    call_chatlike(Aura)

def test_You():
    fluetnai = You()
    result = fluetnai.create_completion(model="ignored", messages=[
        {"role": "user", "content": "如何使用python"}])
    for item in result:
        print(item)


def test_Phind():
    call_chatlike(Liaobots,model= "gpt-4")
