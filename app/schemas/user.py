from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import Annotated


class UserBase(BaseModel):
    username: Annotated[str, Field(title="Username of freelancer")]
    email: Annotated[EmailStr, Field(title="Email of freelancer")]
    role: Annotated[str, Field(title="Role of freelancer")]
    bio: Annotated[str, Field(default=None)]


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: Annotated[int, Field(title="ID of freelancer")]

    model_config = ConfigDict(from_attributes=True)
