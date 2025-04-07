import pytest
from fastapi.testclient import TestClient
from tests.conftest import login_helper

def test_create_activity(client: TestClient):
    # create user "alice"
    client.post("/api/users/signup", json={
        "email": "alice@example.com",
        "username": "alice",
        "password": "password123"
    })

    # 1) Log in first to get JWT
    login_res = client.post("/api/users/login", json={
        "email": "alice@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]
    
    # 2) Create an activity
    res = client.post(
        "/api/activity/create",
        json={"name": "Leetcode"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert res.status_code == 200, res.text
    data = res.json()
    assert "id" in data
    assert data["name"] == "Leetcode"

def test_record_activity(client: TestClient):
    # create user "alice"
    client.post("/api/users/signup", json={
        "email": "alice@example.com",
        "username": "alice",
        "password": "password123"
    })

    # 1) Log in first
    login_res = client.post("/api/users/login", json={
        "email": "alice@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]

    # 2) Create an activity
    res = client.post(
        "/api/activity/create",
        json={"name": "Leetcode"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert res.status_code == 200, res.text
    created_activity = res.json()
    assert "id" in created_activity
    activity_id = created_activity["id"]

    # Start activity (assuming it exists)
    start_res = client.post(
        "/api/activity/start",
        headers={"Authorization": f"Bearer {token}"},
        json={"activity_id": activity_id}
    )
    assert start_res.status_code == 200
    
    # 3) Record activity
    record_res = client.post(
        "/api/activity/record",
        headers={"Authorization": f"Bearer {token}"},
        json={"activity_id": activity_id}
    )
    assert record_res.status_code == 200, record_res.text
    data = record_res.json()
    assert "streak" in data

def test_list_user_activities(client: TestClient):
    # create user "alice"
    client.post("/api/users/signup", json={
        "email": "alice@example.com",
        "username": "alice",
        "password": "password123"
    })

    # 1) Log in first
    login_res = client.post("/api/users/login", json={
        "email": "alice@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]

    # Start new activity
    create_res = client.post(
        "/api/activity/create",
        json={"name": "Meditation"},
        headers={"Authorization": f"Bearer {token}"}
    )
    activity_id = create_res.json()["id"]

    # Start the activity
    client.post(
        "/api/activity/start",
        json={"activity_id": activity_id},
        headers={"Authorization": f"Bearer {token}"}
    )

    # Check progress
    progress_res = client.get(
        "/api/activity/progress",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert progress_res.status_code == 200
    activities = progress_res.json()
    assert len(activities) > 0
    # find the one with "Meditation"
    found = any(a["activity_name"] == "Meditation" for a in activities)
    assert found

def test_record_activity_invalid_id(client: TestClient):
    # create user "alice"
    client.post("/api/users/signup", json={
        "email": "alice@example.com",
        "username": "alice",
        "password": "password123"
    })

    # 1) Log in first
    login_res = client.post("/api/users/login", json={
        "email": "alice@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]

    response = client.post(
        "/api/activity/record",
        headers={"Authorization": f"Bearer {token}"},
        json={"activity_id": "some-random-uuid"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "User activity not found"

