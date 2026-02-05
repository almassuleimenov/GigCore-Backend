from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import new_session
from app.schemas import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


async def get_db():
    async with new_session() as session:
        yield session


@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
async def get_users_list(db: AsyncSession = Depends(get_db)):
    return await user_service.get_all_users(db)
