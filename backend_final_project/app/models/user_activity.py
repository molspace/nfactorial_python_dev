from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
import uuid

class UserActivity(Base):
    __tablename__ = "user_activities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    activity_id = Column(String, ForeignKey("activities.id"))

    streak = Column(Integer, default=0, nullable=False)
    streak_frozen = Column(Boolean, default=False, nullable=False)
    last_practiced = Column(Date, default=None)
    last_completed_date = Column(Date, default=None)
    has_freeze = Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="activities")
    activity = relationship("Activity", back_populates="user_activities")
