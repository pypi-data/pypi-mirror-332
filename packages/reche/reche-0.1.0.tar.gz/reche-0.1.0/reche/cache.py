from typing import Callable, Any
from functools import wraps
import logging
import pickle
from inspect import iscoroutinefunction

from redis import Redis as SyncRedis
from redis.asyncio import Redis as AsyncRedis

from .utils import generate_key


logger = logging.getLogger(__name__)


class RedisCache:
    def __init__(
        self,
        redis_client: SyncRedis | AsyncRedis,
        key_prefix: str = "",
        serializer: Callable[[Any], str | bytes] = pickle.dumps,
        deserializer: Callable[[bytes | Any], Any] = pickle.loads,
        hash_func: str | None = None,
    ):
        self.redis_client = redis_client
        self.key_prefix = key_prefix
        self.serializer = serializer
        self.deserializer = deserializer
        self.hash_func = hash_func

    def cache(
        self,
        ttl: int = 0,
    ) -> Callable:
        """
        Декоратор для кеширования результатов функции в Redis.

        :param ttl: Время жизни записи в секундах (0 — бессрочно).
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def sync_wrapper(*args, **kwargs) -> Any:
                cache_key = generate_key(
                    func, args, kwargs, self.serializer, self.key_prefix, self.hash_func
                )

                if cache_result := self.redis_client.get(cache_key):
                    return self.deserializer(cache_result)

                result = func(*args, **kwargs)

                serialized_result = self.serializer(result)
                ex_time = ttl if ttl > 0 else None
                self.redis_client.set(cache_key, serialized_result, ex=ex_time)

                return result

            @wraps(func)
            async def async_wrapper(*args, **kwargs) -> Any:
                cache_key = generate_key(
                    func, args, kwargs, self.serializer, self.key_prefix, self.hash_func
                )

                if cache_result := await self.redis_client.get(cache_key):
                    return self.deserializer(cache_result)

                if iscoroutinefunction(func):
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)

                serialized_result = self.serializer(result)
                ex_time = ttl if ttl > 0 else None
                await self.redis_client.set(cache_key, serialized_result, ex=ex_time)

                return result

            if isinstance(self.redis_client, SyncRedis):
                return sync_wrapper
            else:
                return async_wrapper

        return decorator
