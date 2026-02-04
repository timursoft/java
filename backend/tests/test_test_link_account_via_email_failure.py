def test_link_account_via_email_failure(api_client, mocker):
    """
    Test that linking an account with an invalid email fails correctly.
    """
    # Arrange
    mock_response = {'status': 'error', 'message': 'Invalid email address.'}
    mocker.patch('external_service.link_account', return_value=mock_response)
    invalid_email = 'invalid-email'
    data = {'email': invalid_email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 400, "Expected status code 400 for invalid email"
    assert response.json() == mock_response, "Expected error response for invalid email"