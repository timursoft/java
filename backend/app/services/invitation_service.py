from backend.app.models.user import Invitation
from backend.app.utils.email_util import send_email
from backend.app import db
from loguru import logger

class InvitationService:
    @staticmethod
    def send_invitation_email(invited_by_user_id: int, emails: list[str]) -> None:
        """Send invitation emails to a list of provided emails."""
        logger.info("Sending invitations for user id {}", invited_by_user_id)
        for email in emails:
            if not validate_email(email):
                logger.error("Invalid email address: {}", email)
                continue
            invitation = Invitation(email=email, invited_by_user_id=invited_by_user_id)
            invitation.generate_referral_link()
            db.session.add(invitation)
            try:
                send_email(to=email, subject="You're Invited!", body=f"Join us using this link: {invitation.referral_link}")
                db.session.commit()
                logger.info("Invitation sent to {}", email)
            except Exception as e:
                db.session.rollback()
                logger.error("Failed to send invitation to {}: {}", email, str(e))

def validate_email(email: str) -> bool:
    """Validate the email address format."""
    # Basic email validation logic
    return '@' in email and '.' in email