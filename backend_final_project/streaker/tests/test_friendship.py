import pytest
from fastapi.testclient import TestClient
from tests.conftest import login_helper, default_user

def test_add_friend_twice(client: TestClient):
    default_user_data = default_user(client)
    token = login_helper(client, email=default_user_data['email'], password=default_user_data['password'])
    # Create a second user to friend
    second_user = {
        "email": "friend@example.com",
        "username": "frienduser",
        "password": "password123"
    }
    res = client.post("/api/users/signup", json=second_user)
    assert res.status_code == 200

    # Get second user's id
    second_user_data = client.post("/api/users/login", json={
        "email": second_user["email"],
        "password": second_user["password"]
    }).json()

    second_user_data = res.json()  # This should have "id" if your signup returns UserRead
    friend_id = second_user_data["id"]

    # Add friend the first time
    response = client.post(
        "/api/friends/add",
        headers={"Authorization": f"Bearer {token}"},
        json={"friend_id": friend_id}
    )
    assert response.status_code == 200

    # Add friend a second time
    response2 = client.post(
        "/api/friends/add",
        headers={"Authorization": f"Bearer {token}"},
        json={"friend_id": friend_id}
    )
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Already friends"
