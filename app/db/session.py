from sqlalchemy.ext.asyncio import async_sessionmaker
from app.db.base import engine

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    async with new_session() as sessioni:
        yield sessioni
