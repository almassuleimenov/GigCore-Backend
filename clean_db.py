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
        await conn.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE;"))
        print("Данные удалены, но таблицы на месте!")
    await engine.dispose()


asyncio.run(clean())
