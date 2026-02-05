from loguru import logger
from typing import Any

from backend.app.services.email_service import EmailService

class GameplayController:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def on_gameplay_session_end(self, session_details: Any) -> None:
        """
        Triggered when a gameplay session ends.

        :param session_details: Details of the session that ended.
        """
        try:
            duration = session_details.get('duration', 0)
            recipient_email = session_details.get('email')
            feedback_link = session_details.get('feedback_link')

            if duration > 60 and recipient_email:
                self.email_service.send_feedback_request_email(recipient_email, feedback_link)
                logger.info("Feedback request email triggered for session ending.")
        except Exception as e:
            logger.error("Error handling session end: {}", str(e))
