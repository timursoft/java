def test_leaderboard_top_10_scores_success(test_client, mock_get_top_scores):
    """
    Test that the leaderboard endpoint returns the top 10 scores successfully.
    """
    # Arrange
    expected_scores = [{'username': 'user1', 'score': 100}, {'username': 'user2', 'score': 95}, ...]  # 10 items
    mock_get_top_scores.return_value = expected_scores

    # Act
    response = test_client.get("/api/leaderboard")

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == expected_scores, "Expected response to match the top 10 scores"