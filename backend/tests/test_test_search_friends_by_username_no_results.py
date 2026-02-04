def test_search_friends_by_username_no_results(client, mocker):
    """Test search for friends by non-existent username returns empty list"""
    # Arrange
    search_username = "nonexistent"
    mocker.patch('app.services.friend_service.search_friends', return_value=[])

    # Act
    response = client.get(f'/api/friends/search?username={search_username}')

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == [], "Expected empty list for non-existent username"