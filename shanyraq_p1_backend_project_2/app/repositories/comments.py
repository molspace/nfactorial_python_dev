from sqlalchemy.orm import Session
from app.database.models import User, Comment, Listing
from app.schemas.comments import CommentCreate, CommentResponse, CommentResponseList
from fastapi import HTTPException
from typing import List

class CommentsRepository:
    def add_comment(self, listing_id: int, comment_data: CommentCreate, db: Session, user: User):
        comment = Comment(
            content=comment_data.content,
            user_id=user.id,
            listing_id=listing_id
        )
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    def get_comments_by_listing_id(self, listing_id: int, db: Session) -> List[Comment]:
        comments = db.query(Comment).filter(Comment.listing_id == listing_id).all()
        if not comments:
            raise HTTPException(status_code=404, detail="Comment not found or unauthorized")
        
        comments_list = [
            CommentResponse(
                id=comment.id,
                user_id=comment.user_id,
                listing_id=comment.listing_id,
                content=comment.content,
            )
        for comment in comments
        ]
        return CommentResponseList(comments=comments_list)

    def update_comment(self, listing_id: int, comment_id: int, comment_data: CommentCreate, db: Session, user: User):
        comment = db.query(Comment).filter(Comment.id == comment_id, Comment.user_id == user.id).first()
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found or unauthorized")
        comment.content = comment_data.content
        db.commit()
        db.refresh(comment)
        return comment

    def delete_comment(self, listing_id: int, comment_id: int, db: Session, user: User):
        comment = db.query(Comment).filter(Comment.id == comment_id, Comment.user_id == user.id).first()
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found or unauthorized")
        db.delete(comment)
        db.commit()
        return {"message": "Comment deleted successfully"}
    
    def get_comments_total_number(self, listing_id: int, db: Session) -> Listing:
        listing = db.query(Listing).filter(Listing.id == listing_id).first()
        listing.total_comments = len(self.get_comments_by_listing_id(listing_id, db))
        return listing
