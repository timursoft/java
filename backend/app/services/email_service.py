from loguru import logger
from typing import Any

from backend.app.templates.feedback_email_template import get_feedback_email_template

class EmailService:
    def __init__(self, email_client: Any):
        self.email_client = email_client

    def send_feedback_request_email(self, recipient_email: str, feedback_link: str) -> None:
        """
        Sends a feedback request email to the specified recipient.

        :param recipient_email: The email address of the recipient.
        :param feedback_link: The URL link to the feedback form.
        """
        try:
            subject = "We value your feedback!"
            html_content = get_feedback_email_template(feedback_link)
            self.email_client.send_email(to=recipient_email, subject=subject, html_content=html_content)
            logger.info("Feedback request email sent to {}", recipient_email)
        except Exception as e:
            logger.error("Failed to send feedback request email to {}: {}", recipient_email, str(e))
