def test_score_resets_on_boundary_collision(game):
    """Test that the score resets after a boundary collision."""
    # Arrange
    game.score = 100
    snake = game.snake
    snake.position = game.boundary_position
    
    # Act
    game.check_collision()
    
    # Assert
    assert game.score == 0, "Score should reset to 0 after collision."