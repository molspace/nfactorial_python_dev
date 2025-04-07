from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    referred_by: Optional[str] = None
    referral_code: Optional[str] = None  # optional input

class UserRead(BaseModel):
    id: str
    email: EmailStr
    username: str
    is_premium: bool
    streak: str
    streak_freezes: str
    referral_code: str
    referred_by: Optional[str]
    created_at: datetime
    avatar_url: str
    avatar_path: Optional[str] = None

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLeaderboard(BaseModel):
    username: str
    streak: int
    avatar_url: str
    avatar_path: Optional[str] = None

class UserUpdate(BaseModel):
    email: EmailStr = None
    username: str = None
    password: str = None
    avatar_url: str