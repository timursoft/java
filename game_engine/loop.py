import time
from loguru import logger

class GameLoop:
    def __init__(self, target_fps: int = 60):
        self.target_fps = target_fps
        self.frame_duration = 1.0 / self.target_fps
        self.last_time = time.time()

    def run(self, engine: 'GameEngine') -> None:
        """Run the main game loop."""
        logger.info("Starting game loop...")
        while engine.is_running:
            current_time = time.time()
            elapsed_time = current_time - self.last_time

            if elapsed_time >= self.frame_duration:
                if not engine.is_paused:
                    self.update_game_state()
                    self.render_frame()
                self.last_time = current_time

            time.sleep(max(0, self.frame_duration - (time.time() - current_time)))
        logger.info("Game loop terminated.")

    def update_game_state(self) -> None:
        """Update the game state for the current frame."""
        logger.debug("Updating game state...")
        # Game state update logic here

    def render_frame(self) -> None:
        """Render the current frame."""
        logger.debug("Rendering frame...")
        # Rendering logic here
