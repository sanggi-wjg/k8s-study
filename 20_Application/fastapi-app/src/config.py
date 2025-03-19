import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_DB: int = os.getenv("REDIS_DB", 0)


@lru_cache
def get_settings():
    return Settings()
