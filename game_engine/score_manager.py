from loguru import logger

current_score = 0

def reset_score() -> None:
    global current_score
    current_score = 0
    logger.info("Score reset to 0 after collision")

# Additional scoring functions can be added here
