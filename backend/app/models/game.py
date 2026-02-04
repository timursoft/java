from typing import Any, Dict
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from backend.app.events.game_events import GameCompletedEvent

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    def complete_game(self) -> None:
        """Mark the game as complete and emit a completion event."""
        # Logic to mark game as complete
        event = GameCompletedEvent(game_id=self.id, player_id=self.player_id, score=self.score)
        event.emit()