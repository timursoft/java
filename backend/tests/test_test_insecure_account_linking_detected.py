def test_insecure_account_linking_detected(api_client, mocker):
    """
    Test that insecure account linking is detected and handled properly.
    """
    # Arrange
    mocker.patch('external_service.is_secure', return_value=False)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 403, "Expected status code 403 for insecure linking"
    assert response.json()['message'] == 'Insecure linking detected.', "Expected error message for insecure linking"