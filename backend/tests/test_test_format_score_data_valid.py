def test_format_score_data_valid():
    """Test that score data is correctly formatted for social media."""
    # Arrange
    score_data = {'score': 1000, 'player': 'TestPlayer'}
    expected_format = "Player TestPlayer scored 1000 points!"

    # Act
    formatted_data = format_score_data(score_data)

    # Assert
    assert formatted_data == expected_format, f"Expected {expected_format}, got {formatted_data}"