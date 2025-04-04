from pydantic import BaseModel
from typing import List

class CommentCreate(BaseModel):
    content: str

class CommentResponse(CommentCreate):
    id: int
    user_id: int
    listing_id: int

    class Config:
        from_attributes = True

class CommentResponseList(BaseModel):
    comments: List[CommentResponse]