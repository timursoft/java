def test_visual_indication_on_boundary_collision(game):
    """Test that visual indication is shown on boundary collision."""
    # Arrange
    snake = game.snake
    snake.position = game.boundary_position
    
    # Act
    game.check_collision()
    
    # Assert
    assert game.visual_effects['collision'] is True, "Visual indication should be active on collision."