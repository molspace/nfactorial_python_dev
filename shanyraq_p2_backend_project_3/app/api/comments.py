from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import User
from app.repositories.comments import CommentsRepository
from app.schemas.comments import CommentCreate, CommentResponseList
from app.utils.security import get_current_user

router = APIRouter(prefix="/shanyraks/{id}/comments", tags=["Comments"])
comments_repository = CommentsRepository()

@router.post("/")
def add_comment(
    listing_id: int, 
    comment_data: CommentCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return comments_repository.add_comment(listing_id, comment_data, db, current_user)

@router.get("/", response_model=CommentResponseList)
def get_comments(listing_id: int, db: Session = Depends(get_db)):
    return comments_repository.get_comments_by_listing_id(listing_id, db)

@router.patch("/{comment_id}")
def update_comment(
    listing_id: int, 
    comment_id: int, 
    comment_data: CommentCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return comments_repository.update_comment(listing_id, comment_id, comment_data, db, current_user)

@router.delete("/{comment_id}")
def delete_comment(
    listing_id: int, 
    comment_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return comments_repository.delete_comment(listing_id, comment_id, db, current_user)
