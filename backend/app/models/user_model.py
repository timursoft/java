from sqlalchemy import Column, Integer, String, JSON
from backend.app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    avatar = Column(JSON, nullable=True)  # New avatar field added
