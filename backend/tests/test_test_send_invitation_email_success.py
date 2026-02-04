def test_send_invitation_email_success(client, mocker):
    """Test sending invitation emails successfully."""
    # Arrange
    valid_emails = ['friend1@example.com']
    mock_send_email = mocker.patch('app.email.send_email', return_value=True)
    response = client.post('/invite', json={'emails': valid_emails})

    # Act
    assert response.status_code == 200, "Response status code should be 200 when emails are sent"
    mock_send_email.assert_called_once_with(['friend1@example.com']), "send_email should be called once with valid emails"