import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).resolve().parents[1] / '.env'
print(f"Loading environment variables from: {env_path}")
load_dotenv(dotenv_path=env_path)

# JWT Settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables.")
