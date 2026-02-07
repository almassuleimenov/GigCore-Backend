import hashlib
from passlib.context import CryptContext
import datetime
import jwt
from datetime import timezone, timedelta
from app.core.config import settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES =   int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)

def create_access_token(data: dict, expires_data: timedelta | None = None) -> str:
    to_encode = data.copy()

    if expires_data:
        expire = datetime.datetime.now(timezone.utc) + expires_data
    else:
        expire = datetime.datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


pwq_context = CryptContext(schemes=["bcrypt"], bcrypt__ident="2b", deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwq_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    
    return pwq_context.verify(password, hashed_password)
