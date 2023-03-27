from loguru import logger

from .logger_config import install
from .loggers import logger as DEFAULT_LOGGER


install()

fluent_logger = logger
