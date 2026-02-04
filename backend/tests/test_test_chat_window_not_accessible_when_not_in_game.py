def test_chat_window_not_accessible_when_not_in_game(client):
    """Test that the chat window cannot be accessed when not in a game."""
    # Arrange
    # Client not in a game session
    # Act
    response = client.get('/game/chat/window')
    # Assert
    assert response.status_code == 403, "Chat window should not be accessible when not in a game"