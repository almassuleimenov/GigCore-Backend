import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
import os
from dotenv import load_dotenv
from app.db import get_db
from app.models import User
from sqlalchemy import select

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
) -> User:
    creden_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentals",
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
