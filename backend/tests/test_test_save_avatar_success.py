def test_save_avatar_success(mock_db_session, test_client):
    """
    Test that the customized avatar is successfully saved to the user profile.
    """
    # Arrange
    avatar_data = {'hair': 'blonde', 'eyes': 'blue', 'outfit': 'formal'}
    user_id = 1

    # Act
    response = test_client.post(f'/users/{user_id}/avatar', json=avatar_data)

    # Assert
    assert response.status_code == 200, "Expected status code to be 200, got {response.status_code}"
    assert response.json() == {'message': 'Avatar saved successfully'}, "Unexpected response message"
    user_avatar = mock_db_session.query(User).filter_by(id=user_id).one().avatar
    assert user_avatar == avatar_data, "Avatar data not saved correctly to the user profile"