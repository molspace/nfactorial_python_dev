from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, Table, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

# models.py

favorite_listings = Table(
    "favorite_listings",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("listing_id", Integer, ForeignKey("listings.id"))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    favorites = relationship("Listing", secondary=favorite_listings, backref="favorited_by")

    listings = relationship("Listing", back_populates="owner")
    comments = relationship("Comment", back_populates="author")

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    address = Column(Text, nullable=False)
    area = Column(Float, nullable=False)
    rooms_count = Column(Integer, nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="listings")
    comments = relationship("Comment", back_populates="listing")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    listing_id = Column(Integer, ForeignKey("listings.id"))

    author = relationship("User", back_populates="comments")
    listing = relationship("Listing", back_populates="comments")
