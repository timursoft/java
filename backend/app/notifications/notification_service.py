class NotificationService:
    # Existing methods...

    @staticmethod
    def send_invitation_notification(user_id: int, game_id: int, inviter_id: int) -> None:
        """
        Send a game invitation notification to a user.

        :param user_id: ID of the user to notify
        :param game_id: ID of the game
        :param inviter_id: ID of the user sending the invite
        """
        try:
            # Logic to send notification
            logger.info("Invitation notification sent to user {} for game {} from user {}", user_id, game_id, inviter_id)
        except Exception as e:
            logger.exception("Failed to send invitation notification: {}", e)
