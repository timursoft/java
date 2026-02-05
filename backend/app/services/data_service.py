from backend.app.repositories.data_repository import DataRepository
from redis import Redis
from loguru import logger

redis_client = Redis()

def fetch_data_with_optimization(params: dict) -> dict:
    """Fetch data with optimized query patterns and caching."""
    cache_key = f"data_cache:{params}"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        logger.info("Cache hit for key: {}", cache_key)
        return cached_data

    logger.info("Cache miss for key: {}. Fetching from database.", cache_key)
    data_repo = DataRepository()
    data = data_repo.get_data(params)
    redis_client.set(cache_key, data, ex=3600)  # Cache expiry set to 1 hour
    return data
