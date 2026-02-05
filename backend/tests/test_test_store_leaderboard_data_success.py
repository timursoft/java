def test_store_leaderboard_data_success(db_session, leaderboard_service):
    """Test successful storage of leaderboard data."""
    # Arrange
    data = {'user_id': 'user123', 'score': 1500}

    # Act
    result = leaderboard_service.store_data(data)

    # Assert
    stored_data = db_session.query(Leaderboard).filter_by(user_id='user123').first()
    assert stored_data is not None, "Data should be stored in the database"
    assert stored_data.score == 1500, "Stored score should match the input score"