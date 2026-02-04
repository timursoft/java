def test_format_achievement_data_valid():
    # Arrange
    achievement_data = {
        'title': 'Level Up',
        'description': 'Reached level 10',
        'score': 1500
    }
    expected_format = 'Achievement Unlocked: Level Up - Reached level 10! Score: 1500'
    
    # Act
    formatted_data = format_achievement_data(achievement_data)
    
    # Assert
    assert formatted_data == expected_format, "Achievement data is not formatted correctly"