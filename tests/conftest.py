# tests/conftest.py
import asyncio
import pytest
from httpx import AsyncClient, ASGITransport
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import app
from app.db.session import new_session
from app.db import get_db

# 🔥 МАГИЯ ДЛЯ WINDOWS И PYTEST 🔥
# Мы принудительно создаем один Event Loop на всю сессию тестов.
# Это решает проблему "attached to a different loop".
@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

# Настройка движка
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

# Фикстура базы данных
@pytest.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session
        # Важно: делаем откат изменений после каждого теста, 
        # чтобы база оставалась чистой
        await session.rollback()

# Фикстура клиента
@pytest.fixture(scope="function")
async def async_client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as ac:
        yield ac
    
    app.dependency_overrides.clear()