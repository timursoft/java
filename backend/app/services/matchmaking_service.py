from typing import List
from backend.app.models.player import Player
from backend.app.notifications.notification_service import NotificationService
from backend.app.utils.logging import logger
import asyncio

class MatchmakingService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    async def find_match(self, player: Player, all_players: List[Player]) -> None:
        logger.info('Attempting to find match for player with skill level {}', player.skill_level)
        match_found = False

        # Start time for timeout check
        start_time = asyncio.get_event_loop().time()

        while not match_found and (asyncio.get_event_loop().time() - start_time < 60):
            potential_opponents = [p for p in all_players if p.skill_level == player.skill_level and p != player]
            if potential_opponents:
                opponent = potential_opponents[0]  # For simplicity, select the first available match
                match_found = True
                logger.info('Match found between player {} and opponent {}', player.id, opponent.id)
                self.notification_service.notify_match_found(player, opponent)
            else:
                await asyncio.sleep(5)  # Wait before retrying to avoid busy loop

        if not match_found:
            logger.info('No match found for player {} within 60 seconds', player.id)