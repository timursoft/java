def test_no_data_loss_during_transitions(mock_game_server, device):
    """Ensure no data loss during transitions."""
    # Arrange
    initial_state = {'level': 1, 'score': 100}
    mock_game_server.set_state(device, initial_state)

    # Act
    mock_game_server.disconnect(device)
    mock_game_server.progress(device, {'level': 2, 'score': 200})  # Simulate update during disconnection
    mock_game_server.reconnect(device)
    result_state = mock_game_server.get_state(device)

    # Assert
    assert result_state == {'level': 2, 'score': 200}, "Data was lost during transition"