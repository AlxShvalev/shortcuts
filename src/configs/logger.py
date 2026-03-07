from logging import getLogger
from logging.config import dictConfig

from pydantic import BaseModel


class LoggingConfig(BaseModel):
    LOGGER_NAME: str = "shortcuts-service"
    LOG_FORMAT: str = "%(levelname)s | %(asctime)s | %(message)s | %(filename)s | %(lineno)s | %(funcName)20s"
    LOG_LEVEL: str = "INFO"

    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        }
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


dictConfig(LoggingConfig().model_dump())
logger = getLogger(LoggingConfig().LOGGER_NAME)