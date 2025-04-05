import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False)
    streak = Column(String, default="0")
    streak_freezes = Column(String, default="0")
    referral_code = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4())[:8])
    referred_by = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    activities = relationship("UserActivity", back_populates="user")
