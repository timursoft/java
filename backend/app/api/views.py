from fastapi import APIRouter, Depends
from backend.app.services.data_service import fetch_data_with_optimization
from loguru import logger

router = APIRouter()

@router.get("/data")
async def get_data(params: dict):
    """API endpoint to fetch data with performance optimizations."""
    try:
        data = await fetch_data_with_optimization(params)
        return {"status": "success", "data": data}
    except Exception as e:
        logger.error("Error fetching data: {}", str(e))
        return {"status": "error", "message": "Failed to fetch data."}
