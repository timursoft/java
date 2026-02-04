def test_share_invitation_link_no_auth(client):
    """
    Test that sharing an invitation link without authentication fails.
    """
    # Arrange
    client.headers.pop('Authorization', None)  # Remove auth header if exists
    invitation_link = '/invite/link'
    response_data = {'platform': 'twitter', 'link': invitation_link}

    # Act
    response = client.post('/api/share-invitation', json=response_data)

    # Assert
    assert response.status_code == 401, "Expected status code to be 401 for unauthenticated request, got {response.status_code}"
    assert response.json()['detail'] == 'Not authenticated', "Expected 'Not authenticated' error message"