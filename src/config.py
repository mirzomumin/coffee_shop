import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings:
    DB_URL: str = os.environ["DB_URL"]
    SECRET_KEY: str = os.environ["SECRET_KEY"]
    ALGORITHM: str = os.environ["ALGORITHM"]
    ACCESS_TOKEN_EXPIRE_SECONDS: int = int(os.environ["ACCESS_TOKEN_EXPIRE_SECONDS"])
    REFRESH_TOKEN_EXPIRE_SECONDS: int = int(os.environ["REFRESH_TOKEN_EXPIRE_SECONDS"])
    TEST_DB_URL: str = os.environ["TEST_DB_URL"]
    DOCS_URL: str | None = os.environ.get("DOCS_URL", None)
    OPENAPI_URL: str | None = os.environ.get("OPENAPI_URL", None)
    REDOC_URL: str | None = os.environ.get("REDOC_URL", None)
    REDIS_HOST: str = os.environ["REDIS_HOST"]
    REDIS_PORT: int = os.environ["REDIS_PORT"]


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "coffee_shop"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }


settings = Settings()
