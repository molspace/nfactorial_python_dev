from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import User
from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.repositories.users import UsersRepository
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import get_current_user

router = APIRouter(prefix="/auth/users", tags=["Authorization"])
users_repository = UsersRepository()

@router.post("/", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return users_repository.create_user(user_data, db)

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return users_repository.login_user(form_data, db)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/me")
def update_user(
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return users_repository.update_user(current_user, user_data, db)

@router.get("/get_all_users_for_debug")
def get_all_users_for_debug(
    db: Session = Depends(get_db)
):
    return db.query(User).all()

@router.post("/favorites/shanyraks/{listing_id}")
def add_listing_to_favorites(
    listing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return users_repository.add_to_favorites(current_user, listing_id, db)

@router.get("/favorites/shanyraks")
def get_favorite_listings(
    current_user: User = Depends(get_current_user)
):
    return {"shanyraks": users_repository.get_favorite_listings(current_user)}

@router.delete("/favorites/shanyraks/{listing_id}")
def remove_favorite_listing(
    listing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return users_repository.remove_favorite_listing(current_user, listing_id, db)
