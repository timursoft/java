def test_real_time_update_with_high_latency(mock_game_server, device):
    """Test game progress updates with high network latency."""
    # Arrange
    initial_state = {'level': 1, 'score': 100}
    mock_game_server.set_state(device, initial_state)

    # Act
    mock_game_server.set_latency(device, 1000)  # 1000 ms latency
    mock_game_server.progress(device, {'level': 2, 'score': 200})
    result_state = mock_game_server.get_state(device)

    # Assert
    assert result_state == {'level': 2, 'score': 200}, "Game progress did not update correctly under high latency"