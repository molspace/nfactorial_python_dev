from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import User
from app.repositories.listings import ListingsRepository
from app.schemas.listings import ListingCreate, ListingUpdate, ListingResponse, ListingResponseComments
from app.utils.security import get_current_user

router = APIRouter(prefix="/shanyraks", tags=["Listings"])
listings_repository = ListingsRepository()

@router.post("/")
def create_listing(
    listing_data: ListingCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return listings_repository.create_listing(listing_data, db, current_user)

# get a listing without total comments info
# @router.get("/{listing_id}", response_model=ListingResponse)
# def get_listing_by_id(
#     listing_id: int, 
#     db: Session = Depends(get_db)
# ):
#     return listings_repository.get_listing_by_id(listing_id, db)

@router.patch("/{listing_id}")
def update_listing(
    listing_id: int, 
    listing_data: ListingUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return listings_repository.update_listing(listing_id, listing_data, db, current_user)

@router.delete("/{listing_id}")
def delete_listing(
    listing_id: int,
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return listings_repository.delete_listing(listing_id, db, current_user)

# get a listing with total comments count
@router.get("/{listing_id}", response_model=ListingResponseComments)
def get_listing_with_comments_number(listing_id: int, db: Session = Depends(get_db)):
    return listings_repository.get_listing_with_comments_number(listing_id, db)