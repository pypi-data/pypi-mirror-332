import logging
import time
from typing import Literal

import redis
from reche import RedisCache


logger = logging.getLogger(__name__)


def get_redis_cache(
    serializer: Literal["json", "pickle"] = "json",
    hash_func: str | None = None,
    key_prefix: str = "",
):
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    if serializer == "json":
        import json

        ser = json.dumps
        deser = json.loads
    elif serializer == "pickle":
        import pickle

        ser = pickle.dumps
        deser = pickle.loads

    return RedisCache(
        redis_client,
        serializer=ser,
        deserializer=deser,
        hash_func=hash_func,
        key_prefix=key_prefix,
    )


def test_sum_json():
    rcache = get_redis_cache(serializer="json")
    rcache.redis_client.flushdb()

    @rcache.cache()
    def sum(a: int, b: int) -> int:
        time.sleep(1)
        return a + b

    result = sum(1, 2)
    assert result == 3

    result = sum(a=1, b=2)
    assert result == 3

    result = sum(b=2, a=1)
    assert result == 3

    assert (
        rcache.redis_client.get(
            'tests.test_sync.test_sum_json.<locals>.sum:{"a": 1, "b": 2}'
        )
        == b"3"
    )
    assert rcache.redis_client.dbsize() == 1


def test_sum_pickle():
    rcache = get_redis_cache(serializer="pickle")
    rcache.redis_client.flushdb()

    @rcache.cache()
    def sum(a: int, b: int) -> int:
        time.sleep(1)
        return a + b

    result = sum(1, 2)
    assert result == 3

    result = sum(a=1, b=2)
    assert result == 3

    result = sum(b=2, a=1)
    assert result == 3

    assert (
        rcache.redis_client.get(
            r"tests.test_sync.test_sum_pickle.<locals>.sum:b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94K\x01\x8c\x01b\x94K\x02u.'"
        )
        == b"\x80\x04K\x03."
    )
    assert rcache.redis_client.dbsize() == 1


def test_greeting_json():
    rcache = get_redis_cache(serializer="json")
    rcache.redis_client.flushdb()

    @rcache.cache()
    def greeting(name: str) -> str:
        time.sleep(1)
        return f"Hello, {name}!"

    result = greeting("Alice")
    assert result == "Hello, Alice!"

    result = greeting("Alice")
    assert result == "Hello, Alice!"

    assert (
        rcache.redis_client.get(
            'tests.test_sync.test_greeting_json.<locals>.greeting:{"name": "Alice"}'
        )
        == b'"Hello, Alice!"'
    )
    assert rcache.redis_client.dbsize() == 1


def test_greeting_pickle():
    rcache = get_redis_cache(serializer="pickle")
    rcache.redis_client.flushdb()

    @rcache.cache()
    def greeting(name: str) -> str:
        time.sleep(1)
        return f"Hello, {name}!"

    result = greeting("Alice")
    assert result == "Hello, Alice!"

    result = greeting("Alice")
    assert result == "Hello, Alice!"

    assert (
        rcache.redis_client.get(
            r"tests.test_sync.test_greeting_pickle.<locals>.greeting:b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\x05Alice\x94s.'"
        )
        == b"\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\rHello, Alice!\x94."
    )
    assert rcache.redis_client.dbsize() == 1


def test_ttl():
    rcache = get_redis_cache(serializer="pickle")
    rcache.redis_client.flushdb()

    @rcache.cache(ttl=5)
    def sum(a: int, b: int) -> int:
        return a + b

    assert rcache.redis_client.dbsize() == 0
    result = sum(1, 2)
    assert result == 3

    assert rcache.redis_client.dbsize() == 1
    time.sleep(3)
    assert rcache.redis_client.dbsize() == 1

    time.sleep(3)
    assert rcache.redis_client.dbsize() == 0


def test_prefix():
    rcache = get_redis_cache(serializer="json", key_prefix="myprefix_")
    rcache.redis_client.flushdb()

    @rcache.cache()
    def greeting(name: str) -> str:
        return f"Hello, {name}!"

    result = greeting("Alice")
    assert result == "Hello, Alice!"

    assert (
        rcache.redis_client.get(
            'myprefix_tests.test_sync.test_prefix.<locals>.greeting:{"name": "Alice"}'
        )
        == b'"Hello, Alice!"'
    )
    assert rcache.redis_client.dbsize() == 1
