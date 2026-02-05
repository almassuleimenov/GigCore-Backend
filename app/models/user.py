from app.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)

    role: Mapped[str] = mapped_column(String, default="freelancer")

    bio: Mapped[str] = mapped_column(Text, nullable=True)

    jobs_posted: Mapped[list["Job"]] = relationship("Job", back_populates="author")
