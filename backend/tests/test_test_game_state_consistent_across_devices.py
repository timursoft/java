def test_game_state_consistent_across_devices(mock_game_server, mobile_device, web_device):
    """Test game state consistency across devices."""
    # Arrange
    initial_state = {'level': 1, 'score': 100}
    mock_game_server.set_state(mobile_device, initial_state)

    # Act
    mock_game_server.progress(mobile_device, {'level': 2, 'score': 200})
    result_state = mock_game_server.get_state(web_device)

    # Assert
    assert result_state == {'level': 2, 'score': 200}, "Game state is not consistent across devices"