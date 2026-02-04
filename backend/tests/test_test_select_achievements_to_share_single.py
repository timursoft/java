def test_select_achievements_to_share_single():
    # Arrange
    achievements = [
        {'id': 1, 'title': 'First Blood'},
        {'id': 2, 'title': 'Sharp Shooter'},
    ]
    selected_ids = [1]
    
    # Act
    selected_achievements = select_achievements_to_share(achievements, selected_ids)
    
    # Assert
    assert len(selected_achievements) == 1, "User should be able to select a single achievement to share"
    assert selected_achievements[0]['title'] == 'First Blood', "Incorrect achievement selected"