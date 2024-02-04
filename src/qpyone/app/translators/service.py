import os
import secrets
from typing import List

from box import Box
from fastapi import UploadFile

from qpyone.app.translators.models import Document, TranslateResult
from qpyone.clients.openai_client import call_openai
from qpyone.compnents.extractors.md_extractor import MarkdownExtractor
from qpyone.compnents.extractors.office_extractor import CSVTextExtractor, \
    PPTTextExtractor
from qpyone.compnents.extractors.pdf_extractor import PdfTextExtractor

extractors = Box({
    "md": MarkdownExtractor(),
    "pdf": PdfTextExtractor(),
    "csv": CSVTextExtractor(),
    "ppt": PPTTextExtractor()
})


async def get_document_from_file(file: UploadFile, file_extract_type: str) -> Document:
    extractor = extractors.get(file_extract_type)
    extracted_text = extractor.extract_text_from_filepath(file)
    doc = Document(text=extracted_text)

    return doc


async def save_translate_result(content_list: List[TranslateResult], file_folder: str) -> str:
    token = secrets.token_hex(16)
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)

    with open(f"{file_folder}/{token}.txt", "w+") as f:
        for i in range(len(content_list)):
            f.write(content_list[i].translated_content)

    return token


async def get_translate_results(texts: List[Document], translate_type: str, api_type: str) -> List[TranslateResult]:
    results = []
    sys_prompt = os.environ[translate_type.upper()]
    for text in texts:
        response = await call_openai(sys_prompt=sys_prompt, user_prompt=text.text, api_type=api_type)
        if response:
            choices = response["choices"]
            completion = choices[0].message.content.strip()
            result = TranslateResult(original_content=text.text, translated_content=completion)
            results.append(result)

    return results
