from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.database import Base

class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_session_id = Column(Integer, ForeignKey('game_sessions.id'))
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')
    game_session = relationship('GameSession')

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            user_id=data.get('user_id'),
            game_session_id=data.get('game_session_id'),
            text=data.get('text')
        )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'game_session_id': self.game_session_id,
            'text': self.text,
            'timestamp': self.timestamp.isoformat(),
            'user': self.user.username
        }
