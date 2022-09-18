from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, nullable=True)

    def dict(self):
        return {
            "user_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "created": self.created,
            "updated": self.updated,
        }

