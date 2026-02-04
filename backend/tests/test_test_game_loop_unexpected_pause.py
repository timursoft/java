def test_game_loop_unexpected_pause(game):
    """Test the behavior of the game loop when paused unexpectedly during a frame update."""
    # Arrange
    game.start_loop()
    
    # Act
    game.pause_unexpectedly()
    
    # Assert
    assert game.is_paused(), "Game should be paused unexpectedly"