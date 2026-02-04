def test_game_pause_resume(game):
    """Test that the game loop can be paused and resumed."""
    # Arrange
    game.start_loop()
    
    # Act
    game.pause()
    is_paused = game.is_paused()
    game.resume()
    is_running = not game.is_paused()
    
    # Assert
    assert is_paused, "Game should be paused"
    assert is_running, "Game should be resumed after being paused"