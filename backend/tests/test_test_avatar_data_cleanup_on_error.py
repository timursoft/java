def test_avatar_data_cleanup_on_error(mock_db_session, test_client):
    """
    Test that no avatar data is saved when an error occurs during saving.
    """
    # Arrange
    invalid_avatar_data = {'hair': 'green'}  # Missing other fields
    user_id = 1

    # Act
    response = test_client.post(f'/users/{user_id}/avatar', json=invalid_avatar_data)

    # Assert
    assert response.status_code == 400, "Expected status code to be 400, got {response.status_code}"
    user_avatar = mock_db_session.query(User).filter_by(id=user_id).one().avatar
    assert user_avatar is None, "Expected no avatar data to be saved when an error occurs"