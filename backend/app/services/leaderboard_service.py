# Import necessary modules
from typing import List, Dict
from backend.app.models.leaderboard_model import LeaderboardEntry
from backend.app.utils.redis_cache import cache
from backend.app.db.database import SessionLocal
from loguru import logger

class LeaderboardService:
    def __init__(self, db_session: SessionLocal):
        self.db_session = db_session

    @cache
    def get_leaderboard(self) -> List[Dict[str, any]]:
        """
        Retrieves the current leaderboard ranking from the database.
        Utilizes caching for high performance.
        """
        try:
            logger.info("Fetching leaderboard from database")
            leaderboard_entries = self.db_session.query(LeaderboardEntry).order_by(LeaderboardEntry.score.desc()).all()
            return [entry.to_dict() for entry in leaderboard_entries]
        except Exception as e:
            logger.error("Failed to fetch leaderboard: {}", e)
            raise

    def update_leaderboard(self, user_id: int, score: int) -> None:
        """
        Updates a user's score in the leaderboard. If the user is not present, they are added.
        This method ensures the leaderboard is updated in real-time.
        """
        try:
            logger.info("Updating leaderboard for user_id: {}", user_id)
            entry = self.db_session.query(LeaderboardEntry).filter_by(user_id=user_id).first()
            if entry:
                entry.score = score
            else:
                entry = LeaderboardEntry(user_id=user_id, score=score)
                self.db_session.add(entry)
            self.db_session.commit()
        except Exception as e:
            logger.error("Failed to update leaderboard for user_id {}: {}", user_id, e)
            self.db_session.rollback()
            raise