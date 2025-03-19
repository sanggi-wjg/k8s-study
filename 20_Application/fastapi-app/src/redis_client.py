import pickle
from typing import Any, Optional

import redis

from src.config import get_settings

config = get_settings()


class RedisClient:
    def __init__(self):
        self.client = redis.StrictRedis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB,
        )

    def get_client(self):
        return self.client

    def set(self, key: str, value: Any, ttl: int = 10):
        self.client.set(key, pickle.dumps(value), ex=ttl)

    def get(self, key: str) -> Optional[Any]:
        cached_value = self.client.get(key)
        if cached_value is None:
            return None

        return pickle.loads(cached_value)

    def get_or_set(self, key: str, value: Any, ttl: int = 10) -> Any:
        cached_value = self.get(key)
        if cached_value is not None:
            return cached_value

        self.set(key, value, ttl)
        return value


redis_client = RedisClient()


def get_redis_client():
    return redis_client
