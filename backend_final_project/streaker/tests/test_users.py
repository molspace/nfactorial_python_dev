import pytest
from fastapi.testclient import TestClient

@pytest.mark.order(1)  # optional: ensures order if you want
def test_signup(client: TestClient):
    payload = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "password123"
    }
    response = client.post("/api/users/signup", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data

@pytest.mark.order(2)
def test_login(client: TestClient):
    # signup
    payload = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "password123"
    }
    client.post("/api/users/signup", json=payload)
    # login
    payload = {
        "email": "testuser@example.com",
        "password": "password123"
    }
    response = client.post("/api/users/login", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_signup_invalid_email(client: TestClient):
    response = client.post("/api/users/signup", json={
        "email": "not_an_email",
        "username": "abc",
        "password": "password123"
    })
    assert response.status_code == 422, response.text  # Pydantic validation should fail

def test_signup_duplicate_email(client: TestClient):
    # First user creation
    client.post("/api/users/signup", json={
        "email": "duplicate@example.com",
        "username": "userone",
        "password": "pass1"
    })
    # Attempt second user creation with same email
    response = client.post("/api/users/signup", json={
        "email": "duplicate@example.com",
        "username": "usertwo",
        "password": "pass2"
    })
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Email already registered"

def test_unauthenticated_access(client: TestClient):
    response = client.get("/api/users/me")
    assert response.status_code == 401
