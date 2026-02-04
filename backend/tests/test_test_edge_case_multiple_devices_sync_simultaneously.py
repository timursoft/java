def test_edge_case_multiple_devices_sync_simultaneously(mock_game_server, device_one, device_two):
    """Test simultaneous sync across multiple devices."""
    # Arrange
    initial_state_device_one = {'level': 1, 'score': 100}
    initial_state_device_two = {'level': 1, 'score': 150}
    mock_game_server.set_state(device_one, initial_state_device_one)
    mock_game_server.set_state(device_two, initial_state_device_two)

    # Act
    mock_game_server.sync(device_one)
    mock_game_server.sync(device_two)
    result_state_device_one = mock_game_server.get_state(device_one)
    result_state_device_two = mock_game_server.get_state(device_two)

    # Assert
    assert result_state_device_one == result_state_device_two, "Game states are inconsistent across devices"