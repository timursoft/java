from backend.app.models.user_model import User
from backend.app.database import db_session
from loguru import logger

class AvatarService:
    @staticmethod
    def save_avatar(user_id: int, avatar_data: dict) -> bool:
        """Saves the customized avatar to the user profile."""
        try:
            user = db_session.query(User).filter(User.id == user_id).first()
            if not user:
                logger.error("User with id {} not found", user_id)
                return False
            user.avatar = avatar_data
            db_session.commit()
            logger.info("Avatar saved successfully for user id {}", user_id)
            return True
        except Exception as e:
            logger.exception("Failed to save avatar for user id {}: {}", user_id, e)
            return False
