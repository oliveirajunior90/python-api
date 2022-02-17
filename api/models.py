from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime

from api.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.now, index=True, nullable=False)
