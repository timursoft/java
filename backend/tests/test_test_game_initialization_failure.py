def test_game_initialization_failure(game):
    """Test that the game initialization fails when a critical component is missing."""
    # Arrange
    game.remove_critical_component()
    
    # Act & Assert
    with pytest.raises(Exception, match="Critical component missing"):
        game.initialize()