def test_game_ends_on_boundary_collision(game):
    """Test that the game ends when the snake hits the boundary."""
    # Arrange
    snake = game.snake
    snake.position = game.boundary_position
    
    # Act
    game.check_collision()
    
    # Assert
    assert game.is_over is True, "Game should end when the snake hits the boundary."