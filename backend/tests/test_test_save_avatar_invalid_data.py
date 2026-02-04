def test_save_avatar_invalid_data(mock_db_session, test_client):
    """
    Test saving avatar with invalid data results in error.
    """
    # Arrange
    invalid_avatar_data = {'hair': '', 'eyes': 'unknown', 'outfit': 'none'}
    user_id = 1

    # Act
    response = test_client.post(f'/users/{user_id}/avatar', json=invalid_avatar_data)

    # Assert
    assert response.status_code == 400, "Expected status code to be 400, got {response.status_code}"
    assert response.json() == {'error': 'Invalid avatar data'}, "Unexpected error message for invalid data"