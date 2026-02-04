def test_no_collision_game_continues(game):
    """Test that the game continues when there is no collision with the boundary."""
    # Arrange
    snake = game.snake
    snake.position = game.safe_position
    
    # Act
    game.check_collision()
    
    # Assert
    assert game.is_over is False, "Game should continue when there is no collision."