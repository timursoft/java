@pytest.mark.asyncio
def test_leaderboard_real_time_updates(test_client, mock_get_top_scores, mock_live_score_updates):
    """
    Test that leaderboard updates in real-time when new scores are added.
    """
    # Arrange
    initial_scores = [{'username': 'user1', 'score': 100}, {'username': 'user2', 'score': 95}, ...]  # 10 items
    updated_scores = [{'username': 'user3', 'score': 105}, {'username': 'user1', 'score': 100}, ...]  # New top score
    mock_get_top_scores.return_value = initial_scores

    # Act
    response = test_client.get("/api/leaderboard")
    assert response.json() == initial_scores, "Expected initial scores to match response"

    # Simulate real-time update
    mock_live_score_updates.send(updated_scores)

    # Assert
    response = test_client.get("/api/leaderboard")
    assert response.json() == updated_scores, "Expected updated scores to reflect real-time changes"