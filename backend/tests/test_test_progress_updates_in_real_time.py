def test_progress_updates_in_real_time(mock_game_server, device):
    """Test real-time update of game progress."""
    # Arrange
    initial_state = {'level': 1, 'score': 100}
    mock_game_server.set_state(device, initial_state)

    # Act
    mock_game_server.progress(device, {'level': 2, 'score': 200})
    result_state = mock_game_server.get_state(device)

    # Assert
    assert result_state == {'level': 2, 'score': 200}, "Game progress did not update in real-time"