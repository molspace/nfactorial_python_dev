from pydantic import BaseModel

class FriendAdd(BaseModel):
    friend_id: str  # or friend_email

class FriendRead(BaseModel):
    id: str
    user_id: str
    friend_id: str