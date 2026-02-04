def test_game_resets_after_collision(game):
    """Test that the game resets properly after a collision is detected and handled."""
    # Arrange
    snake = game.snake
    snake.position = game.boundary_position
    game.check_collision()
    
    # Act
    game.reset()
    
    # Assert
    assert game.is_over is False, "Game should reset and not be over after reset."