"""Initial tables user and job

Revision ID: 5af9659186a9
Revises:
Create Date: 2026-02-04 20:19:48.933228

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "5af9659186a9"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. СОЗДАЕМ ТАБЛИЦУ USERS (Она должна быть первой!)
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False, server_default="freelancer"),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # Индексы для быстрого поиска
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)

    # 2. СОЗДАЕМ ТАБЛИЦУ JOBS (Она ссылается на users)
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("budget", sa.Integer(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "OPEN", "IN_PROGRESS", "REVIEW", "DONE", "CANCELED", name="jobstatus"
            ),
            nullable=False,
        ),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    # Удаляем в обратном порядке: сначала ту, что ссылается, потом ту, на которую ссылаются
    op.drop_table("jobs")
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    # Удаляем тип Enum, чтобы не мусорил
    sa.Enum(name="jobstatus").drop(op.get_bind())
