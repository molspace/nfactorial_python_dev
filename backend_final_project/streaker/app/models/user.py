import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
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

    # TODO:
    referral_code = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4())[:8])
    # referral_code = Column(String, unique=True, index=True)

    # TODO: 
    # referred_by = Column(String, nullable=True)
    referred_by = Column(String, ForeignKey("users.id"), nullable=True)  # FK to another user's id
    # Optional: relationship to referred user (the "referrer")
    referrer = relationship("User", remote_side=[id], backref="referrals")

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    activities = relationship("UserActivity", back_populates="user")

    avatar_path = Column(String, nullable=True)
    # default avatar if none uploaded
    @property
    def avatar_url(self):
        # TODO: set a proper default avatar path
        return self.avatar_path or "https://example.com/default-avatar.png"