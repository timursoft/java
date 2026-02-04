def test_enter_email_addresses_invalid(client):
    """Test entering invalid email addresses."""
    # Arrange
    invalid_emails = ['invalid-email', 'another-invalid-email']
    response = client.post('/invite', json={'emails': invalid_emails})

    # Act
    assert response.status_code == 400, "Response status code should be 400 for invalid emails"
    assert 'error' in response.json(), "Response should contain error message"