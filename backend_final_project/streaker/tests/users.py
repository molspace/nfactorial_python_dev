import requests

url = "http://127.0.0.1:8000/api/users/signup"
payload = {
    "email": "testuser@example.com",
    "username": "testuser",
    "password": "password123",
    "referred_by": None
}

response = requests.post(url, json=payload)
print("Signup response:")
print(response.status_code, response.json())

url = "http://127.0.0.1:8000/api/users/login"
payload = {
    "email": "testuser@example.com",
    "password": "password123"
}

response = requests.post(url, json=payload)
data = response.json()
token = data.get("access_token")

print("Login response:")
print(response.status_code, data)

if token:
    with open("token.txt", "w") as f:
        f.write(token)
    print("\n✅ Access token saved to token.txt")


# Load token from file
with open("token.txt", "r") as f:
    token = f.read().strip()

url = "http://127.0.0.1:8000/api/users/me"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
print("User info response:")
print(response.status_code, response.json())