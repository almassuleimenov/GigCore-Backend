import asyncio
from redis.asyncio import Redis
from app.core.config import settings

REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT


async def main():
    redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    try:
        await redis.set("test_key", "Hello, Redis!")
        value = await redis.get("test_key")
        print(f"УСПЕШНО ПОДКЛЮЧЕНО К REDIS! Значение test_key: {value}")
    except Exception as e:
        print(f"ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К REDIS: {e}")
    finally:
        await redis.aclose()


if __name__ == "__main__":
    asyncio.run(main())
