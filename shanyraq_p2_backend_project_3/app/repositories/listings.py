from sqlalchemy.orm import Session
from app.database.models import User, Comment, Listing
from app.schemas.listings import ListingCreate, ListingUpdate, ListingResponse
from fastapi import HTTPException
from typing import Optional

class ListingsRepository:
    def create_listing(self, listing_data: ListingCreate, db: Session, user: User):
        new_listing = Listing(**listing_data.dict(), user_id=user.id)
        db.add(new_listing)
        db.commit()
        db.refresh(new_listing)
        return {"id": new_listing.id}

    def get_listing_by_id(self, listing_id: int, db: Session):
        listing = db.query(Listing).filter(Listing.id == listing_id).first()
        if not listing:
            raise HTTPException(status_code=404, detail="Listing not found or unauthorized")
        return listing

    def update_listing(self, listing_id: int, update_data: ListingUpdate, db: Session, user: User):
        listing = db.query(Listing).filter(Listing.id == listing_id, Listing.user_id == user.id).first()
        if not listing:
            raise HTTPException(status_code=404, detail="Listing not found or unauthorized")
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(listing, key, value)
        db.commit()
        db.refresh(listing)
        return {"message": "Listing attributes were updated successfully"}

    def delete_listing(self, listing_id: int, db: Session, user: User):
        listing = db.query(Listing).filter(Listing.id == listing_id, Listing.user_id == user.id).first()
        if not listing:
            raise HTTPException(status_code=404, detail="Listing not found or unauthorized")
        db.delete(listing)
        db.commit()
        return {"message": "Listing deleted successfully"}
    
    def get_listing_with_comments_number(self, listing_id: int, db: Session):
        listing = self.get_listing_by_id(listing_id, db)
        total_comments = db.query(Comment).filter(Comment.listing_id == listing_id).count()
        return {
            **ListingResponse.model_validate(listing).model_dump(),
            "total_comments": total_comments
        }

    def filter_listings(
        db: Session,
        limit: int,
        offset: int,
        type: Optional[str] = None,
        rooms_count: Optional[int] = None,
        price_from: Optional[float] = None,
        price_until: Optional[float] = None,
    ):
        query = db.query(Listing)

        if type:
            query = query.filter(Listing.type == type)
        if rooms_count:
            query = query.filter(Listing.rooms_count == rooms_count)
        if price_from is not None:
            query = query.filter(Listing.price >= price_from)
        if price_until is not None:
            query = query.filter(Listing.price <= price_until)

        total = query.count()

        listings = (
            query.order_by(Listing.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
        
        return {
            "total": total,
            "objects": listings
        }
