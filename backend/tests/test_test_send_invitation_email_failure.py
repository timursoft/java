def test_send_invitation_email_failure(client, mocker):
    """Test failure in sending invitation emails."""
    # Arrange
    valid_emails = ['friend1@example.com']
    mock_send_email = mocker.patch('app.email.send_email', return_value=False)
    response = client.post('/invite', json={'emails': valid_emails})

    # Act
    assert response.status_code == 500, "Response status code should be 500 on email send failure"
    assert 'error' in response.json(), "Response should contain error message when email sending fails"