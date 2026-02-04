from typing import Optional
from backend.app.models import User

class UserService:
    # Existing methods...

    def search_by_username(self, username: str) -> Optional[User]:
        """
        Search for a user by username.

        :param username: Username to search for
        :return: User object if found, None otherwise
        """
        try:
            return User.get_by_username(username)
        except Exception as e:
            logger.exception("Error searching user by username: {}", e)
            return None
