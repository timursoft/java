from loguru import logger

class GameControl:
    def __init__(self, engine: 'GameEngine'):
        self.engine = engine

    def pause(self) -> None:
        """Pause the game loop."""
        if not self.engine.is_paused:
            logger.info("Pausing game...")
            self.engine.is_paused = True

    def resume(self) -> None:
        """Resume the game loop."""
        if self.engine.is_paused:
            logger.info("Resuming game...")
            self.engine.is_paused = False
