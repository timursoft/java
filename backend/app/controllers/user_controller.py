from loguru import logger
from fastapi import APIRouter, HTTPException, Depends
from backend.app.services.user_service import UserService
from backend.app.models.user import User

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int, user_service: UserService = Depends()):
    try:
        user = await user_service.get_user_by_id(user_id)
        if not user:
            logger.error("User with id {} not found", user_id)
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        logger.error("Failed to retrieve user: {}", e)
        raise HTTPException(status_code=500, detail="Internal server error")