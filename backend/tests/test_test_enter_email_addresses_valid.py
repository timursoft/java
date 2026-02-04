def test_enter_email_addresses_valid(client):
    """Test entering valid email addresses."""
    # Arrange
    valid_emails = ['friend1@example.com', 'friend2@example.com']
    response = client.post('/invite', json={'emails': valid_emails})

    # Act
    assert response.status_code == 200, "Response status code should be 200 for valid emails"
    assert response.json()['success'] is True, "Response should indicate success"