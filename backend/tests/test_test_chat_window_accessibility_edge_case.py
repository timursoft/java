def test_chat_window_accessibility_edge_case(high_load_game_session):
    """Test chat window accessibility under high server load."""
    # Arrange
    client = high_load_game_session
    # Act
    response = client.get('/game/chat/window')
    # Assert
    assert response.status_code == 200, "Chat window should be accessible under high load"