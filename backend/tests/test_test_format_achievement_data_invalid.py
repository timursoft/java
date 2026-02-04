def test_format_achievement_data_invalid():
    # Arrange
    achievement_data = {
        'title': 'Level Up',
        # Missing 'description' and 'score'
    }
    
    # Act & Assert
    with pytest.raises(KeyError, match="Missing fields in achievement data"):
        format_achievement_data(achievement_data)