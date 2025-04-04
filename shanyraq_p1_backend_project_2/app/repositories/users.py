from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.users import UserCreate, UserUpdate
from app.utils.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from datetime import timedelta

class UsersRepository:
    def create_user(self, user_data: UserCreate, db: Session):
        user_exists = db.query(User).filter(User.username == user_data.username).first()
        if user_exists:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = hash_password(user_data.password)
        db_user = User(
            username=user_data.username,
            phone=user_data.phone,
            password=hashed_password,
            name=user_data.name,
            city=user_data.city
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def login_user(self, form_data: OAuth2PasswordRequestForm, db: Session):
        user = db.query(User).filter(User.username == form_data.username).first()
        if not user or not verify_password(form_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token}

    def update_user(self, user: User, user_data: UserUpdate, db: Session):
        db_user = db.query(User).filter(User.id == user.id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return {"message": "User attributes were updated successfully"}