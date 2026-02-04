def test_invitation_link_redirect_error(client):
    """
    Test that an error is returned if the invitation link fails to redirect.
    """
    # Arrange
    invalid_link = '/invite/invalid-link'

    # Act
    response = client.get(invalid_link, follow_redirects=True)

    # Assert
    assert response.status_code == 404, "Expected status code to be 404 for invalid link, got {response.status_code}"
    assert 'Page not found' in response.text, "Expected 'Page not found' message for invalid link"