from pydantic import BaseModel
from typing import Optional
from datetime import date

class ActivityProgress(BaseModel):
    activity_id: str
    activity_name: str
    streak: int
    streak_frozen: bool
    has_freeze: bool = False
    last_practiced: Optional[date]
    last_completed_date: Optional[date]
