# Reche (Redis Cache)

> Python библиотека, которая предоставляет декоратор для кэширования результатов функций в Redis, поддерживая различные форматы сериализации и стратегии кэширования, а также асинхронные операции.

## Установка
- pip:
```bash
pip install git+https://gitlab.com/Randommist/reche.git
```
- uv:
```bash
uv add git+https://gitlab.com/Randommist/reche.git
```
- poetry:
```bash
poetry add git+https://gitlab.com/Randommist/reche.git
```

## Использование (sync)
```python
import time
import redis
from reche import RedisCache


redis_client = redis.Redis(host="localhost", port=6379, db=0)
rcache = RedisCache(redis_client)

@rcache.cache()
def sum(a: int, b: int) -> int:
    time.sleep(3)
    return a + b

result = sum(1, 2)  # ожидание 3 секунды
print(result)

result = sum(1, 2)  # моментально
print(result)
```

## Использование (async)
```python
import asyncio
import redis.asyncio as redis
from reche import RedisCache


redis_client = redis.Redis(host="localhost", port=6379, db=0)
rcache = RedisCache(redis_client)

@rcache.cache()
async def sum(a: int, b: int) -> int:
    await asyncio.sleep(3)
    return a + b

async def main():
    result = await sum(1, 2)  # ожидание 3 секунды
    print(result)

    result = await sum(1, 2)  # моментально
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```
