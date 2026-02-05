import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL").replace("postgresql://", "postgresql+asyncpg://")


async def clean():
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        # CASCADE принудительно удаляет таблицу, даже если на неё кто-то ссылается
        await conn.execute(text("DROP TABLE users CASCADE;"))
        print("База очищена от старого мусора!")
    await engine.dispose()


asyncio.run(clean())
