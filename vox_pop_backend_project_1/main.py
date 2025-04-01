from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import datetime

app = FastAPI()

# temporary in-memory storage for comments
comments = []

class Comment(BaseModel):
    text: str
    category: str
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now(datetime.timezone.utc))

@app.post("/comment", status_code=201)
def post_comment(comment: Comment):
    comments.append(comment)
    return {"message": "Comment added successfully!"}

@app.get("/comments", response_model=List[Comment])
@app.get("/comments/{page}", response_model=List[Comment])
def get_comments(page: int = 1, limit: int = 5):
    if page < 1:
        raise HTTPException(status_code=400, detail="Page number must be at least 1")
    
    offset = (page - 1) * limit
    sorted_comments = sorted(comments, key=lambda c: c.timestamp, reverse=False)
    return sorted_comments[offset : offset + limit]

@app.get("/")
def read_root():
    return {"message": "Welcome to VoxPop!"}
