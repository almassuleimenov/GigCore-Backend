from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from redis.asyncio import Redis
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.core import verify_password, create_access_token
from app.models import User
from app.api.deps import get_redis , oauth2_scheme


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    query = select(User).where(User.email == form_data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")

async def logout(
    token : str = Depends(oauth2_scheme), redis : Redis =  Depends(get_redis)
):
    await redis.set(f"blacklist:{token}","loggeed_out", ex=1800)
    
    return {
        "message" : "Successfully logged out"
    }
