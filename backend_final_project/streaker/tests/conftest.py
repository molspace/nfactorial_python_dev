import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.session import Base, get_db

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test DB schema for each test session
@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Optional teardown logic
    Base.metadata.drop_all(bind=engine)

# Override the get_db dependency to use the test DB
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)

def login_helper(client: TestClient, email="test@example.com", password="testpass"):
    res = client.post("/api/users/login", json={"email": email, "password": password})
    return res.json()["access_token"]

@pytest.fixture
def create_user(client: TestClient):
    """
    Returns a function for creating a user with given email, username, password.
    Returns a dict containing at least 'email', 'username', 'password', and any other response data.
    """
    def _create_user(email: str, username: str, password: str = "password123"):
        payload = {"email": email, "username": username, "password": password}
        res = client.post("/api/users/signup", json=payload)
        assert res.status_code in [200, 201], res.text
        data = res.json()  # This has "id", "email", "username", etc. from your UserRead schema
        # Add password so we can log in with it later
        data["password"] = password
        return data
    return _create_user

def default_user(client):
    # sign up user if not already
    user_data = {"email": "test@example.com", "username": "testuser", "password": "testpass"}
    res = client.post("/api/users/signup", json=user_data)
    return user_data  # or res.json()

@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

