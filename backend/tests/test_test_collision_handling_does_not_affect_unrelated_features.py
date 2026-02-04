def test_collision_handling_does_not_affect_unrelated_features(game, mocker):
    """Ensure unrelated game features are unaffected by collision handling."""
    # Arrange
    snake = game.snake
    snake.position = game.boundary_position
    unrelated_feature = mocker.patch('game.unrelated_feature')
    
    # Act
    game.check_collision()
    
    # Assert
    unrelated_feature.assert_not_called(), "Unrelated features should not be triggered by collision handling."