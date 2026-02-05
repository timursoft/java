from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.services.leaderboard_service import LeaderboardService
from backend.app.db.database import get_db

router = APIRouter()

@router.get("/leaderboard/", response_model=List[Dict[str, any]])
def read_leaderboard(db: Session = Depends(get_db)):
    leaderboard_service = LeaderboardService(db)
    try:
        return leaderboard_service.get_leaderboard()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve leaderboard")

@router.post("/leaderboard/update/")
def update_leaderboard(user_id: int, score: int, db: Session = Depends(get_db)):
    leaderboard_service = LeaderboardService(db)
    try:
        leaderboard_service.update_leaderboard(user_id, score)
        return {"message": "Leaderboard updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not update leaderboard")