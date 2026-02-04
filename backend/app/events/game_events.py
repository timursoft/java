from typing import Any, Dict
from backend.app.listeners.leaderboard_listener import LeaderboardListener

class GameCompletedEvent:
    def __init__(self, game_id: int, player_id: int, score: int) -> None:
        self.game_id = game_id
        self.player_id = player_id
        self.score = score

    def emit(self) -> None:
        """Emit the game completed event."""
        listener = LeaderboardListener()
        listener.handle(self.to_dict())

    def to_dict(self) -> Dict[str, Any]:
        return {
            'game_id': self.game_id,
            'player_id': self.player_id,
            'score': self.score
        }