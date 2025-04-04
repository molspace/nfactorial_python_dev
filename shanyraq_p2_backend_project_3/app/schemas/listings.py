from pydantic import BaseModel
from typing import Optional

class ListingCreate(BaseModel):
    type: str
    price: float
    address: str
    area: float
    rooms_count: int
    description: Optional[str] = None

class ListingResponse(ListingCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True # allows Pydantic to accept SQLAlchemy objects and convert them to dicts

class ListingUpdate(BaseModel):
    type: str = None
    price: float = None
    address: str = None
    area: float = None
    rooms_count: int = None
    description: Optional[str] = None

class ListingResponseComments(ListingResponse):
    total_comments: int