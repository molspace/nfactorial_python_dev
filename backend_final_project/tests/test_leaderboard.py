import pytest
from fastapi.testclient import TestClient

def test_leaderboard_order(create_user, client: TestClient):
    userA_payload = create_user("leaderA@example.com", "leaderA", "password123")
    userB_payload = create_user("leaderB@example.com", "leaderB", "password456")

    # 3) Log in as userA
    login_a_res = client.post("/api/users/login", json={
        "email": userA_payload["email"],
        "password": userA_payload["password"]
    })
    assert login_a_res.status_code == 200, login_a_res.text
    tokenA = login_a_res.json()["access_token"]

    # 4) Log in as userB
    login_b_res = client.post("/api/users/login", json={
        "email": userB_payload["email"],
        "password": userB_payload["password"]
    })
    assert login_b_res.status_code == 200, login_b_res.text
    tokenB = login_b_res.json()["access_token"]

    # 5) Artificially increase userA's streak (assuming your app has some route to do so)
    # For example, userA can "complete" an activity multiple times
    # If your app doesn't have an easy way, you can force the streak in the DB or do repeated calls.

    # -- create an activity for userA
    create_activity_a = client.post(
        "/api/activity/create",
        json={"name": "Chess"},
        headers={"Authorization": f"Bearer {tokenA}"}
    )
    activity_id_a = create_activity_a.json()["id"]

    # -- start that activity
    client.post(
        "/api/activity/start",
        json={"activity_id": activity_id_a},
        headers={"Authorization": f"Bearer {tokenA}"}
    )

    # -- record or complete it multiple times to push streak up
    for _ in range(3):
        client.post(
            "/api/activity/complete",
            json={"activity_id": activity_id_a},
            headers={"Authorization": f"Bearer {tokenA}"}
        )

    # 6) For userB, do fewer completions so userB ends with a smaller streak
    create_activity_b = client.post(
        "/api/activity/create",
        json={"name": "Piano"},
        headers={"Authorization": f"Bearer {tokenB}"}
    )
    activity_id_b = create_activity_b.json()["id"]

    client.post(
        "/api/activity/start",
        json={"activity_id": activity_id_b},
        headers={"Authorization": f"Bearer {tokenB}"}
    )

    # Just 1 completion for userB
    client.post(
        "/api/activity/complete",
        json={"activity_id": activity_id_b},
        headers={"Authorization": f"Bearer {tokenB}"}
    )

    # 7) Now fetch the leaderboard
    leaderboard_res = client.get("/api/users/leaderboard")
    assert leaderboard_res.status_code == 200, leaderboard_res.text

    leaderboard_data = leaderboard_res.json()
    # e.g. something like:
    # [
    #   {"username": "leaderA", "streak": 3},
    #   {"username": "leaderB", "streak": 1},
    #   ...
    # ]

    # 8) Check if userA's streak is >= userB's streak
    #    and that userA is ranked higher
    # We'll assume the top is index 0
    if len(leaderboard_data) >= 2:
        assert leaderboard_data[0]["username"] == "leaderA"
        assert leaderboard_data[0]["streak"] >= leaderboard_data[1]["streak"]

    # If you want, you can also confirm userB is at index 1
    # or find them by username in the list.

    # 9) (Optional) Clean up or leave data as-is
    # depends on your test strategy
