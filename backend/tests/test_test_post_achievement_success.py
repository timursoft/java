def test_post_achievement_success(mock_social_media_api):
    # Arrange
    achievement_data = 'Achievement Unlocked: Level Up!'
    mock_social_media_api.post.return_value = {'status': 'success', 'message': 'Posted successfully'}
    
    # Act
    response = post_achievement_to_social_media(achievement_data)
    
    # Assert
    assert response['status'] == 'success', "Achievement post did not succeed"
    assert response['message'] == 'Posted successfully', "Unexpected confirmation message"