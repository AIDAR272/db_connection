import requests


ENDPOINT = "http://127.0.0.1:8000"


def test_get():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_post():
    payload = {
        "name": "Aidar",
        "lastname": "Nasirov",
        "age": 20,
        "email": "example.com"
    }
    response = requests.post(ENDPOINT + "/user", json=payload)
    assert response.status_code == 200


def test_put(user_id: int):
    payload = {
  "name": "string",
  "lastname": "string",
  "age": 0,
  "email": "string"
}
    response = requests.put(ENDPOINT + f"/{user_id}", json=payload)
    assert response.status_code == 200


def test_delete(user_id: int):
    response = requests.delete(ENDPOINT + f"/{user_id}")
    assert response.status_code == 200