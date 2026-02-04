def test_avatar_persistence_across_sessions(mock_db_session, test_client):
    """
    Test that avatar changes are persistent across sessions.
    """
    # Arrange
    avatar_data = {'hair': 'red', 'eyes': 'green', 'outfit': 'casual'}
    user_id = 1
    test_client.post(f'/users/{user_id}/avatar', json=avatar_data)

    # Simulate a new session by re-instantiating the client
    new_test_client = TestClient(app)

    # Act
    response = new_test_client.get(f'/users/{user_id}/avatar')

    # Assert
    assert response.status_code == 200, "Expected status code to be 200, got {response.status_code}"
    assert response.json() == avatar_data, "Avatar data not persistent across sessions"