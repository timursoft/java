def test_post_achievement_failure(mock_social_media_api):
    # Arrange
    achievement_data = 'Achievement Unlocked: Level Up!'
    mock_social_media_api.post.return_value = {'status': 'failure', 'message': 'API error'}
    
    # Act
    response = post_achievement_to_social_media(achievement_data)
    
    # Assert
    assert response['status'] == 'failure', "Expected failure status"
    assert response['message'] == 'API error', "Incorrect error message returned"