def test_format_leaderboard_for_facebook_with_empty_data(test_client):
    """Test formatting leaderboard for Facebook with empty data."""
    # Arrange
    empty_data = {}
    # Act
    response = test_client.post("/share/facebook", json=empty_data)
    # Assert
    assert response.status_code == 400, "Should return 400 status when data is empty"