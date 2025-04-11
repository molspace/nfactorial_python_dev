import uuid
from sqlalchemy import Column, String, ForeignKey
from app.db.session import Base

class Friendship(Base):
    __tablename__ = "friendships"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    friend_id = Column(String, ForeignKey("users.id"))
