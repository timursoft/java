def test_store_data_invalid_format(leaderboard_service):
    """Test storing leaderboard data with invalid format raises error."""
    # Arrange
    invalid_data = {'user_id': 'user123', 'points': 1500}  # Wrong key 'points'

    # Act / Assert
    with pytest.raises(ValueError, match="Invalid data format"):
        leaderboard_service.store_data(invalid_data)