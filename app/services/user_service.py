from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import User
from app.schemas import UserCreate


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:

    user_data = user_in.model_dump()

    password = user_data.pop("password")

    new_user = User(**user_data, password_hash=password + "_hashed")

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def get_all_users(session: AsyncSession) -> list[User]:
    query = select(User)

    result = await session.execute(query)

    return result.scalars().all()
