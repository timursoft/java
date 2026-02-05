from loguru import logger
from backend.app.services.email_service import send_feedback_email
from apscheduler.schedulers.background import BackgroundScheduler

# Assuming that we have a way to track gameplay and get user emails

def schedule_feedback_email(user_email: str, gameplay_duration: int, feedback_form_link: str) -> None:
    """
    Schedule a feedback email to be sent after a specific gameplay duration.
    :param user_email: Email address of the user.
    :param gameplay_duration: Gameplay duration in seconds.
    :param feedback_form_link: Link to the feedback form.
    """
    scheduler = BackgroundScheduler()
    try:
        scheduler.add_job(
            func=send_feedback_email,
            trigger='interval',
            seconds=gameplay_duration,
            args=[user_email, feedback_form_link],
            id=f'feedback_email_{user_email}'
        )
        scheduler.start()
        logger.info("Scheduled feedback email for {} after {} seconds", user_email, gameplay_duration)
    except Exception as e:
        logger.error("Failed to schedule feedback email for {}: {}", user_email, e)