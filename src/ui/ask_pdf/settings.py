import os

from box import Box
from dotenv import load_dotenv, find_dotenv, dotenv_values
from pydantic_settings import BaseSettings, SettingsConfigDict

_ = load_dotenv(find_dotenv())  # read local .env file
base_env_config = Box(dotenv_values(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      extra="ignore",
                                      arbitrary_types_allowed=True)
    base_env_config: Box = base_env_config


default_settings = Settings()
