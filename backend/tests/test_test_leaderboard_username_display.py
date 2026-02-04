def test_leaderboard_username_display(test_client, mock_get_top_scores):
    """
    Test that usernames are correctly displayed alongside scores.
    """
    # Arrange
    scores = [{'username': 'user1', 'score': 100}, {'username': 'user2', 'score': 95}, ...]  # 10 items
    mock_get_top_scores.return_value = scores

    # Act
    response = test_client.get("/api/leaderboard")

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    for score in response.json():
        assert 'username' in score, "Expected each score entry to have a username"
        assert 'score' in score, "Expected each score entry to have a score"