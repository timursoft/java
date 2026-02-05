def test_retrieve_leaderboard_data_success(db_session, leaderboard_service):
    """Test successful retrieval of leaderboard data."""
    # Arrange
    db_session.add(Leaderboard(user_id='user123', score=1500))
    db_session.commit()

    # Act
    result = leaderboard_service.retrieve_data('user123')

    # Assert
    assert result is not None, "Data should be retrieved successfully"
    assert result['score'] == 1500, "Retrieved score should match the stored score"