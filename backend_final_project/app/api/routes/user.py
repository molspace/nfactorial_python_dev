from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, UserLogin, UserLeaderboard, UserUpdate
from app.crud.user import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token
from fastapi.responses import JSONResponse
from datetime import timedelta
from app.core.auth import get_current_user
from app.models.user import User
from sqlalchemy import desc
from app.db.session import get_db
import uuid
import os

router = APIRouter()

# Signup route
@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = create_user(db, user)
    return new_user

# Login route
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create JWT token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Get user profile route
@router.get("/me", response_model=UserRead)
def read_users_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, current_user.email)
    return db_user

# Update route
@router.patch("/me")
def update_user(user_data: UserUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user_data:
        raise HTTPException(status_code=400, detail="No update data provided")
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return {"message": "Updated successfully"}

# Upload avatar route
AVATAR_DIR = "app/static/avatars"
os.makedirs(AVATAR_DIR, exist_ok=True)

@router.post("/me/avatar/upload")
def upload_avatar(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    ext = os.path.splitext(file.filename)[-1]
    if ext.lower() not in [".png", ".jpg", ".jpeg", ".gif"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    filename = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(AVATAR_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    user.avatar_path = file_path
    db.commit()
    db.refresh(user)

    return {"message": "Avatar uploaded successfully", "avatar_path": file_path}

# Remove avatar route
@router.post("/me/avatar/remove")
def remove_avatar(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.avatar_path:
        try:
            if os.path.exists(user.avatar_path):
                os.remove(user.avatar_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting file: {e}")

        user.avatar_path = None
        db.commit()

    return {"message": "Avatar removed successfully"}

# Referrals route
@router.get("/me/referrals", response_model=list[str])
def get_referrals(db: Session = Depends(get_db), user=Depends(get_current_user)):
    referrals = db.query(User).filter(User.referred_by_id == user.id).all()
    return [r.email for r in referrals]

# Leaderboard route
@router.get("/leaderboard", response_model=list[UserLeaderboard])
def get_leaderboard(db: Session = Depends(get_db)):
    top_users = db.query(User).order_by(desc(User.streak)).limit(10).all()
    return [UserLeaderboard(username=user.username, streak=int(user.streak), avatar_url=user.avatar_url, avatar_path=user.avatar_path) for user in top_users]