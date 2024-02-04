import mimetypes
import pypdf

from qpyone.compnents.extractors.models import TextContextExtractor, validate_mimetype


class PdfTextExtractor(TextContextExtractor):

    def extract_text_from_filepath(self, file_path: str) -> str:
        self.validate_file_type(file_path)
        reader = pypdf.PdfReader(file_path)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()
        return extracted_text

    def validate_file_type(self, file_path: str):
        # Get the mimetype of the file based on its extension
        validate_mimetype(file_path, [".pdf"], "application/pdf")
