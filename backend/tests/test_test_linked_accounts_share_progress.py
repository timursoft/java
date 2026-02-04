def test_linked_accounts_share_progress(api_client, mocker):
    """
    Test that linked accounts correctly share progress.
    """
    # Arrange
    mock_progress = {'level': 10, 'score': 5000}
    mocker.patch('external_service.get_shared_progress', return_value=mock_progress)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()['progress'] == mock_progress, "Expected shared progress data"