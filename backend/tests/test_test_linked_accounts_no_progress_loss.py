def test_linked_accounts_no_progress_loss(api_client, mocker):
    """
    Test that no progress is lost when linking accounts.
    """
    # Arrange
    initial_progress = {'level': 10, 'score': 5000}
    mocker.patch('external_service.get_progress', return_value=initial_progress)
    mocker.patch('external_service.get_shared_progress', return_value=initial_progress)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()['progress'] == initial_progress, "Expected no progress loss"