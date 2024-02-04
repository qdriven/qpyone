from pydantic import BaseModel, Field


class OpenAIPdfViewModels(BaseModel):
    api_key: Field(None, alias="apiKey")

