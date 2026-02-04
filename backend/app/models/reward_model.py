from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from backend.app.database import Base


class Reward(Base):
    __tablename__ = 'rewards'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    user = relationship('User', back_populates='rewards')

    def __init__(self, user_id: int, type: str, description: str = None):
        self.user_id = user_id
        self.type = type
        self.description = description
