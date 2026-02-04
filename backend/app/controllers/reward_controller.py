from backend.app.models.reward_model import Reward
from backend.app.database import db_session
from backend.app.utils.logger import logger


def credit_user_reward(user_id: int) -> None:
    """
    Credit a reward to the user account for successful invitation.
    """
    try:
        new_reward = Reward(user_id=user_id, type='invitation', description='Reward for successful invitation')
        db_session.add(new_reward)
        db_session.commit()
        logger.info("Reward credited to user id {}", user_id)
    except Exception as e:
        db_session.rollback()
        logger.error("Failed to credit reward to user id {}: {}", user_id, str(e))
