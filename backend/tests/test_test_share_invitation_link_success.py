def test_share_invitation_link_success(client, mock_social_media_api):
    """
    Test that a registered user can successfully share an invitation link via social media.
    """
    # Arrange
    mock_social_media_api.return_value = {'status': 'success', 'message': 'Link shared'}
    invitation_link = '/invite/link'
    response_data = {'platform': 'twitter', 'link': invitation_link}

    # Act
    response = client.post('/api/share-invitation', json=response_data)

    # Assert
    assert response.status_code == 200, "Expected status code to be 200, got {response.status_code}"
    assert response.json() == {'status': 'success'}, "Expected successful sharing response"