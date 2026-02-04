def test_search_friends_by_username_success(client, mocker):
    """Test successful search for friends by username"""
    # Arrange
    search_username = "friend123"
    mock_response = [{"username": "friend123", "status": "online"}]
    mocker.patch('app.services.friend_service.search_friends', return_value=mock_response)

    # Act
    response = client.get(f'/api/friends/search?username={search_username}')

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == mock_response, "Response JSON does not match expected"