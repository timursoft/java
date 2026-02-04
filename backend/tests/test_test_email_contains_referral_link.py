def test_email_contains_referral_link(client, mocker):
    """Test that the email contains a unique referral link."""
    # Arrange
    valid_emails = ['friend1@example.com']
    referral_link = 'http://example.com/referral?code=unique-code'
    mock_send_email = mocker.patch('app.email.send_email', return_value=True)
    mock_generate_link = mocker.patch('app.referral.generate_referral_link', return_value=referral_link)
    response = client.post('/invite', json={'emails': valid_emails})

    # Act
    assert response.status_code == 200, "Response status code should be 200 when referral link is generated"
    mock_generate_link.assert_called_once(), "generate_referral_link should be called once"
    mock_send_email.assert_called_once_with(['friend1@example.com'], referral_link), "send_email should be called with referral link"