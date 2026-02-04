def test_leaderboard_top_10_scores_empty(test_client, mock_get_top_scores):
    """
    Test leaderboard endpoint returns empty list when there are no scores.
    """
    # Arrange
    mock_get_top_scores.return_value = []

    # Act
    response = test_client.get("/api/leaderboard")

    # Assert
    assert response.status_code == 200, "Expected status code to be 200 even when no scores exist"
    assert response.json() == [], "Expected response to be an empty list when no scores are present"