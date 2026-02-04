from backend.app.models.user_model import User
from backend.app.models.invitation_model import Invitation
from backend.app.controllers.reward_controller import credit_user_reward
from backend.app.utils.logger import logger


def handle_invitation(invitation_id: int) -> None:
    """
    Handle an invitation by processing the invitation
    and crediting the inviter with a reward if applicable.
    """
    try:
        invitation = Invitation.query.get(invitation_id)
        if not invitation:
            logger.error("Invitation with id {} not found", invitation_id)
            return

        if invitation.is_accepted:
            logger.info("Invitation {} already accepted", invitation_id)
            return

        # Mark the invitation as accepted
        invitation.is_accepted = True
        invitation.save()

        logger.info("Processing reward for invitation id {}", invitation_id)
        credit_user_reward(invitation.inviter_id)

    except Exception as e:
        logger.error("Failed to handle invitation {}: {}", invitation_id, str(e))
