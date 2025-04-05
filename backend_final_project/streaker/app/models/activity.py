from sqlalchemy import Column, String
from app.db.session import Base
import uuid
from sqlalchemy.orm import relationship


class Activity(Base):
    __tablename__ = "activities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)

    user_activities = relationship("UserActivity", back_populates="activity")
