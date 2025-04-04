from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import User
from app.repositories.listings import ListingsRepository
from app.schemas.listings import ListingCreate, ListingUpdate, ListingResponse, ListingResponseComments
from app.utils.security import get_current_user
from typing import Optional

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

@router.get("/")
def get_filtered_listings(
    limit: int = 10,
    offset: int = 0,
    type: Optional[str] = None,
    rooms_count: Optional[int] = None,
    price_from: Optional[float] = None,
    price_until: Optional[float] = None,
    db: Session = Depends(get_db),
):
    result = listings_repository.filter_listings(
        db=db,
        limit=limit,
        offset=offset,
        type=type,
        rooms_count=rooms_count,
        price_from=price_from,
        price_until=price_until
    )

    return {
        "total": result["total"],
        "objects": [
            {
                "_id": l.id,
                "type": l.type,
                "price": l.price,
                "address": l.address,
                "area": l.area,
                "rooms_count": l.rooms_count,
            }
            for l in result["objects"]
        ]
    }
