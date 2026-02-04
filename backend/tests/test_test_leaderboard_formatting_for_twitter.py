def test_leaderboard_formatting_for_twitter(test_client):
    """Test that the leaderboard ranking is formatted correctly for Twitter."""
    # Arrange
    response = test_client.get('/api/leaderboard/format/twitter')
    # Act
    formatted_text = response.json().get('formatted_text')
    # Assert
    assert formatted_text.startswith("Rank:"), "Formatted text should start with 'Rank:'"
    assert len(formatted_text) <= 280, "Formatted text should be within Twitter's character limit."