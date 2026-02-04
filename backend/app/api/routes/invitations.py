from fastapi import APIRouter, HTTPException
from backend.app.services.game_service import GameService
from backend.app.services.user_service import UserService

router = APIRouter()

@router.post("/invite")
async def invite_friend(game_id: int, friend_username: str, current_user_id: int):
    """
    API endpoint to invite a friend to a game.

    :param game_id: ID of the game
    :param friend_username: Username of the friend to invite
    :param current_user_id: ID of the current user sending the invite
    """
    if not GameService().invite_friend(game_id, friend_username, current_user_id):
        raise HTTPException(status_code=400, detail="Failed to send invitation")

@router.get("/search")
async def search_user(username: str):
    """
    API endpoint to search for users by username.

    :param username: Username to search for
    """
    user = UserService().search_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
