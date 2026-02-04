def test_format_leaderboard_for_facebook(test_client, mock_leaderboard):
    """Test that leaderboard ranking is formatted correctly for Facebook."""
    # Arrange
    mock_leaderboard.return_value = {
        "rank": 1,
        "user": "test_user",
        "score": 1500
    }
    # Act
    response = test_client.post("/share/facebook", json=mock_leaderboard.return_value)
    formatted_data = response.json()
    # Assert
    assert formatted_data["message"].startswith("I'm ranked #1"), "Formatted message should start with rank"