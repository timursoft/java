def test_feedback_provided_after_saving(mock_db_session, test_client):
    """
    Test that feedback is provided after saving the avatar.
    """
    # Arrange
    avatar_data = {'hair': 'black', 'eyes': 'brown', 'outfit': 'sporty'}
    user_id = 2

    # Act
    response = test_client.post(f'/users/{user_id}/avatar', json=avatar_data)

    # Assert
    assert response.status_code == 200, "Expected status code to be 200, got {response.status_code}"
    assert 'message' in response.json(), "Expected feedback message in response"
    assert response.json()['message'] == 'Avatar saved successfully', "Unexpected feedback message"