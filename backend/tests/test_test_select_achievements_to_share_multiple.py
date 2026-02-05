def test_select_achievements_to_share_multiple():
    # Arrange
    achievements = [
        {'id': 1, 'title': 'First Blood'},
        {'id': 2, 'title': 'Sharp Shooter'},
        {'id': 3, 'title': 'Master Explorer'},
    ]
    selected_ids = [1, 3]
    
    # Act
    selected_achievements = select_achievements_to_share(achievements, selected_ids)
    
    # Assert
    assert len(selected_achievements) == 2, "User should be able to select multiple achievements to share"
    assert selected_achievements[0]['title'] == 'First Blood', "First achievement selection is incorrect"
    assert selected_achievements[1]['title'] == 'Master Explorer', "Second achievement selection is incorrect"