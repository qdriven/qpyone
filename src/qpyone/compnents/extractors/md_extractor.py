
from qpyone.compnents.extractors.exceptions import ExtractException
from qpyone.compnents.extractors.models import TextContextExtractor, validate_mimetype


class MarkdownExtractor(TextContextExtractor):

    def extract_text_from_filepath(self, file_path: str) -> str:
        mimetype = self.validate_file_type(file_path)
        if mimetype == "text/plain" or mimetype == "text/markdown":
            with open(file_path, "rb") as f:
                extracted_text = f.read().decode("utf-8")
            return extracted_text
        else:
            raise ExtractException("The file should be not a markdown file")

    def validate_file_type(self, file_path: str):
        # Get the mimetype of the file based on its extension
        validate_mimetype(file_path,[".md"],"text/markdown")

