from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.user import User
from app.schemas import UserCreate, UserResponse
from app.services import user_service
from app.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
async def get_users_list(db: AsyncSession = Depends(get_db) , current_user : User =  Depends(get_current_user)):
    return await user_service.get_all_users(db)
