def test_game_initialization_success(game):
    """Test that the game initializes properly."""
    # Arrange & Act
    game.initialize()
    
    # Assert
    assert game.is_initialized == True, "Game should be initialized properly"