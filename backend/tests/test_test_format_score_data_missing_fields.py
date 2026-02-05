def test_format_score_data_missing_fields():
    """Test that missing fields in score data raise an exception."""
    # Arrange
    score_data = {'score': 1000}  # Missing 'player' field

    # Act & Assert
    with pytest.raises(KeyError, match="'player'"):
        format_score_data(score_data)