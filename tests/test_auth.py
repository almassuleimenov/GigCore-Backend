import pytest
from httpx import AsyncClient
from sqlalchemy import select
from app.models.user import User
from app.core import get_password_hash

@pytest.mark.asyncio
async def test_login_success(async_client: AsyncClient, db_session):
    email = "auth_test@example.com"
    password = "strong_password_123"
    hashed = get_password_hash(password)
    
    new_user = User(
        username="auth_tester",
        email=email,
        role="freelancer",
        password_hash=hashed
    )
    db_session.add(new_user)
    await db_session.commit()

    login_data = {
        "username": email, 
        "password": password
    }
    
    response = await async_client.post("/auth/login", data=login_data)

    assert response.status_code == 200, f"Login failed: {response.text}"
    
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    print(f"\n✅ Token received: {token_data['access_token'][:20]}...")

@pytest.mark.asyncio
async def test_login_wrong_password(async_client: AsyncClient):
    login_data = {
        "username": "nobody@example.com",
        "password": "wrong_password"
    }
    
    response = await async_client.post("/auth/login", data=login_data)
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"