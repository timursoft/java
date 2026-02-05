from cache import Cache
from logger import log

class GameStateService:
    def __init__(self, cache: Cache):
        self.cache = cache

    def get_game_state(self, player_id: str) -> dict:
        log.info('Fetching game state for player_id: {}', player_id)
        cached_state = self.cache.get(player_id)
        if cached_state:
            log.info('Cache hit for player_id: {}', player_id)
            return cached_state

        # Logic to fetch game state from a database or other source
        game_state = self._fetch_game_state_from_db(player_id)

        # Cache the game state for future requests
        self.cache.set(player_id, game_state)
        log.info('Cache set for player_id: {}', player_id)

        return game_state

    def _fetch_game_state_from_db(self, player_id: str) -> dict:
        # Placeholder for actual DB fetching logic
        log.info('Fetching game state from DB for player_id: {}', player_id)
        return {}
