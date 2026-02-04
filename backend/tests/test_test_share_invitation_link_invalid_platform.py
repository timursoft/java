def test_share_invitation_link_invalid_platform(client):
    """
    Test that sharing an invitation link with an invalid platform returns an error.
    """
    # Arrange
    invitation_link = '/invite/link'
    response_data = {'platform': 'myspace', 'link': invitation_link}

    # Act
    response = client.post('/api/share-invitation', json=response_data)

    # Assert
    assert response.status_code == 400, "Expected status code to be 400 for invalid platform, got {response.status_code}"
    assert response.json()['detail'] == 'Unsupported platform', "Expected 'Unsupported platform' error message"