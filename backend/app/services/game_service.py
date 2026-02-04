from backend.app.notifications.notification_service import NotificationService
from backend.app.models import User, Game

class GameService:
    # Existing methods...

    def invite_friend(self, game_id: int, friend_username: str, current_user_id: int) -> bool:
        """
        Invite a friend to a game.

        :param game_id: ID of the game
        :param friend_username: Username of the friend to invite
        :param current_user_id: ID of the current user sending the invite
        :return: Boolean indicating success of operation
        """
        try:
            game = Game.get_by_id(game_id)
            if not game:
                logger.error("Game not found: {}", game_id)
                return False

            friend = User.get_by_username(friend_username)
            if not friend:
                logger.error("User not found: {}", friend_username)
                return False

            NotificationService.send_invitation_notification(friend.id, game_id, current_user_id)
            return True
        except Exception as e:
            logger.exception("Failed to invite friend: {}", e)
            return False
