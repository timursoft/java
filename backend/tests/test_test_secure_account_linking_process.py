def test_secure_account_linking_process(api_client, mocker):
    """
    Test that the account linking process uses secure protocols.
    """
    # Arrange
    mocker.patch('external_service.is_secure', return_value=True)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json().get('is_secure'), "Expected secure account linking process"