from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.models.friendship import Friendship
from app.core.auth import get_current_user
from app.schemas.friendship import FriendAdd, FriendRead

router = APIRouter()

@router.post("/add", response_model=FriendRead)
def add_friend(payload: FriendAdd, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Check if friend exists
    friend = db.query(User).filter_by(id=payload.friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")

    # Prevent adding yourself
    if friend.id == user.id:
        raise HTTPException(status_code=400, detail="Cannot add yourself as a friend")

    # Check if already friends
    existing = db.query(Friendship).filter_by(user_id=user.id, friend_id=friend.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already friends")

    friendship = Friendship(user_id=user.id, friend_id=friend.id)
    db.add(friendship)
    db.commit()
    db.refresh(friendship)
    return friendship

@router.get("/", response_model=list[FriendRead])
def list_friends(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    friendships = db.query(Friendship).filter_by(user_id=user.id).all()
    return friendships
