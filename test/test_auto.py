import pytest


@pytest.mark.asyncio
async def test_post(client):
    payload = {
        "name": "Aidar",
        "lastname": "Nasirov",
        "age": 20,
        "email": "example.com"
    }
    response = await client.post("/user", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "User was added"


@pytest.mark.asyncio
async def test_get(client):
    response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_put(client, user_id = 32):
    payload = {
  "name": "stringstring",
  "lastname": "string",
  "age": 0,
  "email": "string"
}
    response = await client.put(f"/{user_id}", json=payload)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete(client, user_id=33):
    response = await client.delete(f"/{user_id}")
    assert response.status_code == 200
