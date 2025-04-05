from pydantic import BaseModel
from typing import Optional
from datetime import date

class ActivityCreate(BaseModel):
    name: str

class UserActivityCreate(BaseModel):
    activity_id: str

class UserActivityRead(BaseModel):
    activity_id: str
    streak: int
    last_practiced: Optional[date]
    streak_frozen: bool

    class Config:
        orm_mode = True