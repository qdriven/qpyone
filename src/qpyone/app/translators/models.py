from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class TranslateResult(BaseModel):
    original_content: str
    translated_content: str


class Document(BaseModel):
    id: Optional[str] = None
    text: str


# TODO: More types to database or configurations
class ApiType(str, Enum):
    open_ai = 'open_ai'
    azure = 'azure'


# TODO: More types to database or configurations
class TranslateType(str, Enum):
    ZH_EN = 'zh_en'
    EN_ZH = 'en_zh'


class TranslateResponse(BaseModel):
    results: List[TranslateResult]


class TranslatedFileResponse(BaseModel):
    result: str
