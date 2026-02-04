from typing import Dict
from backend.app.repositories.leaderboard_repository import LeaderboardRepository
from backend.app.services.notification_service import NotificationService
from backend.app.utils.logging import logger

class LeaderboardService:
    def __init__(self) -> None:
        self.repository = LeaderboardRepository()
        self.notification_service = NotificationService()

    def update_leaderboard(self, event_data: Dict[str, Any]) -> None:
        """Update the leaderboard with the new game results."""
        try:
            # Update the leaderboard in the repository
            self.repository.update_score(event_data)
            # Notify the user about their new ranking
            self.notification_service.notify_user(event_data['player_id'], 'Your new ranking is...')
            logger.info('Leaderboard updated successfully for player_id: {}', event_data['player_id'])
        except Exception as e:
            logger.error('Failed to update leaderboard: {}', str(e))