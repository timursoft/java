from loguru import logger
from backend.app.config import settings
from backend.app.utils.email_client import send_email


def send_feedback_email(user_email: str, feedback_form_link: str) -> None:
    """
    Send a feedback request email to the specified user.
    :param user_email: Email address of the user.
    :param feedback_form_link: Link to the feedback form.
    """
    try:
        subject = "We value your feedback!"
        html_content = render_feedback_email_template(feedback_form_link)
        send_email(to_address=user_email, subject=subject, html_content=html_content)
        logger.info("Feedback email sent to {}", user_email)
    except Exception as e:
        logger.error("Failed to send feedback email to {}: {}", user_email, e)


def render_feedback_email_template(feedback_form_link: str) -> str:
    """
    Render the feedback email template with the provided feedback form link.
    :param feedback_form_link: Link to the feedback form.
    :return: Rendered HTML content.
    """
    return f"""
    <html>
        <body>
            <p>Thank you for participating in our beta testing program!</p>
            <p>We would love to hear your thoughts.</p>
            <p>Please <a href="{feedback_form_link}">click here</a> to provide your feedback.</p>
            <p>Thank you!</p>
        </body>
    </html>
    """