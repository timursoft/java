def test_chat_window_accessible_during_gameplay(game_session):
    """Test that the chat window can be accessed during gameplay."""
    # Arrange
    client = game_session
    # Act
    response = client.get('/game/chat/window')
    # Assert
    assert response.status_code == 200, "Chat window should be accessible during gameplay"