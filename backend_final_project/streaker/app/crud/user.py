from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
import secrets
from fastapi import HTTPException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)

    # Default: no referrer
    referred_by = None

    # Check if referral code is valid
    if user.referral_code:
        referrer = db.query(User).filter_by(referral_code=user.referral_code).first()
        if referrer:
            referred_by = referrer.id
        else:
            raise HTTPException(status_code=400, detail="Invalid referral code")

    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        # referral_code=str(uuid.uuid4())[:8],  # or secrets.token_hex(4)
        referral_code=secrets.token_hex(4),  # Generates a unique referral code
        referred_by=referred_by,       # Stores the referrer’s user ID
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
