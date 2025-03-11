import logging
import asyncio
from typing import Literal

import pytest
import pytest_asyncio
import redis.asyncio as redis
from redis_cache import RedisCache


logger = logging.getLogger(__name__)


def get_redis_cache(
    serializer: Literal["json", "pickle"] = "json", hash_func: str | None = None
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
        redis_client, serializer=ser, deserializer=deser, hash_func=hash_func
    )


@pytest_asyncio.fixture
async def rcache_json():
    db = get_redis_cache(serializer="json")
    await db.redis_client.flushdb()

    yield db

    if isinstance(db.redis_client, redis.Redis):
        await db.redis_client.aclose()


@pytest_asyncio.fixture
async def rcache_pickle():
    db = get_redis_cache(serializer="pickle")
    await db.redis_client.flushdb()

    yield db

    if isinstance(db.redis_client, redis.Redis):
        await db.redis_client.aclose()


@pytest.mark.asyncio
async def test_sum_json(rcache_json):
    rcache: RedisCache = rcache_json

    @rcache.cache()
    async def sum(a: int, b: int) -> int:
        await asyncio.sleep(1)
        return a + b

    # Это так же работает но pyright будет ругаться
    # @rcache.cache()
    # def sync_sum(a: int, b: int) -> int:
    #     time.sleep(1)
    #     return a + b

    # result = await sync_sum(1,2)
    # assert result == 3

    result = await sum(1, 2)
    assert result == 3

    result = await sum(a=1, b=2)
    assert result == 3

    result = await sum(b=2, a=1)
    assert result == 3

    assert (
        await rcache.redis_client.get(
            'tests.test_async.test_sum_json.<locals>.sum:{"a": 1, "b": 2}'
        )
        == b"3"
    )
    assert await rcache.redis_client.dbsize() == 1


@pytest.mark.asyncio
async def test_sum_pickle(rcache_pickle):
    rcache: RedisCache = rcache_pickle

    @rcache.cache()
    async def sum(a: int, b: int) -> int:
        await asyncio.sleep(1)
        return a + b

    result = await sum(1, 2)
    assert result == 3

    result = await sum(a=1, b=2)
    assert result == 3

    result = await sum(b=2, a=1)
    assert result == 3

    assert (
        await rcache.redis_client.get(
            r"tests.test_async.test_sum_pickle.<locals>.sum:b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94K\x01\x8c\x01b\x94K\x02u.'"
        )
        == b"\x80\x04K\x03."
    )
    assert await rcache.redis_client.dbsize() == 1


@pytest.mark.asyncio
async def test_greeting_json(rcache_json):
    rcache: RedisCache = rcache_json

    @rcache.cache()
    async def greeting(name: str) -> str:
        await asyncio.sleep(1)
        return f"Hello, {name}!"

    result = await greeting("Alice")
    assert result == "Hello, Alice!"

    result = await greeting("Alice")
    assert result == "Hello, Alice!"

    assert (
        await rcache.redis_client.get(
            'tests.test_async.test_greeting_json.<locals>.greeting:{"name": "Alice"}'
        )
        == b'"Hello, Alice!"'
    )
    assert await rcache.redis_client.dbsize() == 1


@pytest.mark.asyncio
async def test_greeting_pickle(rcache_pickle):
    rcache: RedisCache = rcache_pickle

    @rcache.cache()
    async def greeting(name: str) -> str:
        await asyncio.sleep(1)
        return f"Hello, {name}!"

    result = await greeting("Alice")
    assert result == "Hello, Alice!"

    result = await greeting("Alice")
    assert result == "Hello, Alice!"

    assert (
        await rcache.redis_client.get(
            r"tests.test_async.test_greeting_pickle.<locals>.greeting:b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\x05Alice\x94s.'"
        )
        == b"\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\rHello, Alice!\x94."
    )
    assert await rcache.redis_client.dbsize() == 1


@pytest.mark.asyncio
async def test_ttl(rcache_pickle):
    rcache: RedisCache = rcache_pickle

    @rcache.cache(ttl=5)
    async def sum(a: int, b: int) -> int:
        await asyncio.sleep(1)
        return a + b

    assert await rcache.redis_client.dbsize() == 0
    result = await sum(1, 2)
    assert result == 3

    assert await rcache.redis_client.dbsize() == 1
    await asyncio.sleep(3)
    assert await rcache.redis_client.dbsize() == 1

    await asyncio.sleep(3)
    assert await rcache.redis_client.dbsize() == 0
