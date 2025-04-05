from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    referred_by: Optional[str] = None

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

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
