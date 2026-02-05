# Import necessary modules
from sqlalchemy import Column, Integer, Index
from backend.app.db.base_class import Base

class LeaderboardEntry(Base):
    __tablename__ = 'leaderboard_entries'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False)
    score = Column(Integer, index=True)

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "score": self.score
        }

    __table_args__ = (
        Index('ix_leaderboard_score', 'score'),
    )