def test_select_achievements_to_share_none():
    # Arrange
    achievements = [
        {'id': 1, 'title': 'First Blood'},
        {'id': 2, 'title': 'Sharp Shooter'},
    ]
    selected_ids = []
    
    # Act
    selected_achievements = select_achievements_to_share(achievements, selected_ids)
    
    # Assert
    assert len(selected_achievements) == 0, "Selecting no achievements should return an empty list"