def test_leaderboard_formatting_for_twitter_edge_case(test_client):
    """Test edge case where leaderboard ranking is unusually high or low."""
    # Arrange
    response = test_client.get('/api/leaderboard/format/twitter', params={'ranking': 9999})
    # Act
    formatted_text = response.json().get('formatted_text')
    # Assert
    assert formatted_text.startswith("Rank:"), "Formatted text should start with 'Rank:'"
    assert "9999" in formatted_text, "Formatted text should correctly include the ranking number."