def test_game_loop_runs_fixed_frame_rate(game):
    """Test that the game loop runs at a fixed frame rate."""
    # Arrange
    desired_frame_rate = 60
    game.set_frame_rate(desired_frame_rate)
    
    # Act
    game.start_loop()
    
    # Assert
    assert game.get_current_frame_rate() == desired_frame_rate, "Game loop should run at the fixed frame rate"