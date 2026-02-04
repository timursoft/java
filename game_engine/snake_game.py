from game_engine.rendering import Event
from game_engine.score_manager import reset_score
from loguru import logger

class SnakeGame:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]  # Snake starts at the center
        self.direction = (0, 1)  # Moving down by default
        self.game_over = False

    def update_state(self) -> None:
        if self.game_over:
            return

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if self._is_collision(new_head):
            self._handle_collision()
            return

        self.snake.insert(0, new_head)
        self.snake.pop()  # Remove the tail piece

    def _is_collision(self, position: tuple[int, int]) -> bool:
        x, y = position
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def _handle_collision(self) -> None:
        logger.info("Collision detected at position: {}", self.snake[0])
        self.game_over = True
        reset_score()
        Event.trigger('collision', position=self.snake[0])