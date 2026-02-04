from backend.app.services.leaderboard_service import LeaderboardService

class LeaderboardListener:
    def handle(self, event_data: dict) -> None:
        """Handle game completion event to update leaderboard."""
        leaderboard_service = LeaderboardService()
        leaderboard_service.update_leaderboard(event_data)