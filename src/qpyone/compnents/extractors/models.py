import abc
import mimetypes
from abc import abstractmethod
from typing import List


class TextContextExtractor(abc.ABC):
    @abstractmethod
    def extract_text_from_filepath(self, file_path: str) -> str:
        """Return the text content of a file given its filepath."""
        pass

    @abstractmethod
    def validate_file_type(self, file_path: str):
        pass


def validate_mimetype(file_path: str,
                      valid_extensions: List[str],
                      valid_mime_type: str):
    mimetype, _ = mimetypes.guess_type(file_path)

    if not mimetype:
        for extension in valid_extensions:
            if file_path.endswith(extension):
                mimetype = valid_mime_type
                break
    else:
        raise Exception("Unsupported file type")
    return mimetype
