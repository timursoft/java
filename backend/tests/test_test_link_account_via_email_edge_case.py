def test_link_account_via_email_edge_case(api_client, mocker):
    """
    Test linking account with an email that includes special characters.
    """
    # Arrange
    mock_response = {'status': 'success', 'message': 'Account linked successfully.'}
    mocker.patch('external_service.link_account', return_value=mock_response)
    special_email = 'test+special@example.com'
    data = {'email': special_email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json() == mock_response, "Expected successful response with special character email"