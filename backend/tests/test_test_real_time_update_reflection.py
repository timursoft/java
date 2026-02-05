def test_real_time_update_reflection(db_session, leaderboard_service, websocket_client):
    """Test real-time update reflection in leaderboard."""
    # Arrange
    data = {'user_id': 'user123', 'score': 1500}
    leaderboard_service.store_data(data)

    # Act
    data_update = {'user_id': 'user123', 'score': 1600}
    leaderboard_service.update_data(data_update)

    # Assert
    websocket_client.send.assert_called_with(data_update)
    stored_data = db_session.query(Leaderboard).filter_by(user_id='user123').first()
    assert stored_data.score == 1600, "Score should be updated to the latest value"