from typing import Optional
from backend.app.models.user import User
from backend.app.database.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            user = await self.user_repository.find_by_id(user_id)
            return user
        except Exception as e:
            logger.error("Error retrieving user from repository: {}", e)
            return None