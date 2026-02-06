import hashlib
from passlib.context import CryptContext
import datetime
import jwt
from datetime import timezone, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


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


pwq_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:

    utf8_password = password.encode("utf_8")

    h = hashlib.sha256(utf8_password).hexdigest()

    return pwq_context.hash(h)


def verify_password(password: str, hashed_password: str) -> bool:

    utf8_password = password.encode("utf_8")

    h = hashlib.sha256(utf8_password).hexdigest()

    return pwq_context.verify(h, hashed_password)
