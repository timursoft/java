def test_leaderboard_top_10_scores_exceeds_limit(test_client, mock_get_top_scores):
    """
    Test leaderboard endpoint handles more than 10 scores properly.
    """
    # Arrange
    scores = [{'username': f'user{i}', 'score': 100-i} for i in range(15)]  # 15 items
    mock_get_top_scores.return_value = scores

    # Act
    response = test_client.get("/api/leaderboard")

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert len(response.json()) == 10, "Expected only top 10 scores to be returned"