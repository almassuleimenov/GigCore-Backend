import jwt
from fastapi import Depends, HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models import User
from sqlalchemy import select
from redis.asyncio import Redis
from app.core.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
async def get_redis() -> Redis: # type: ignore
    
    redis = Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        decode_responses=True,
    )
    
    try:
        yield redis
    finally:
        await redis.aclose()
        
        


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db) , redis : Redis = Depends(get_redis)
) -> User:
    creden_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentals",
    )
    
    token_in_redis = await redis.get(f"blacklist:{token}")
    
    if token_in_redis:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Token has been revoked",
        )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str = payload.get("sub")

        if email is None:
            raise creden_exception
    except jwt.PyJWTError:
        raise creden_exception

    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if user is None:
        raise creden_exception

    return user

