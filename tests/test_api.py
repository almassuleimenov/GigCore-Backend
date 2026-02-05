import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_user_and_job(client: AsyncClient):

    user_payload = {
        "username": "testuser",
        "email": "master@test.com",
        "password": "strongpassword",
        "role": "freelancer",
        "bio": "Experienced developer",
    }

    response = await client.post("/users/", json=user_payload)

    assert response.status_code == 200, "User creation failed"
    data = response.json()
    assert data["email"] == "master@test.com"
    assert "id" in data

    user_id = data["id"]

    job_payload = {
        "title": "Test Job",
        "description": "This is a test job",
        "budget": 1000,
    }

    response = await client.post(f"/jobs/?user_id={user_id}", json=job_payload)
    assert response.status_code == 200, "Job creation failed"
    data = response.json()
    assert data["title"] == "Test Job"
    assert data["status"] == "open"
    assert data["author_id"] == user_id
