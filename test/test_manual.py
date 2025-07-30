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


def test_put():
    payload = {
  "name": "string",
  "lastname": "string",
  "age": 0,
  "email": "string"
}
    response = requests.put(ENDPOINT + "/27", json=payload)
    assert response.status_code == 200


def test_delete():
    response = requests.delete(ENDPOINT + "/4")
    assert response.status_code == 200