from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.security import get_password_hash
from app.models import User
from app.schemas import UserCreate


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user_data = user_in.model_dump()

    password = user_data.pop("password")

    hashed_password = get_password_hash(password)

    new_user = User(**user_data, password_hash=hashed_password)

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def get_all_users(session: AsyncSession) -> list[User]:
    query = select(User)

    result = await session.execute(query)

    return result.scalars().all()
