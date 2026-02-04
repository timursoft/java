def test_link_account_via_email_success(api_client, mocker):
    """
    Test that accounts can be successfully linked via email.
    """
    # Arrange
    mock_response = {'status': 'success', 'message': 'Account linked successfully.'}
    mocker.patch('external_service.link_account', return_value=mock_response)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json() == mock_response, "Expected successful account linkage response"