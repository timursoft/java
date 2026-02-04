def test_redirect_to_registration_page(client):
    """
    Test that the invitation link redirects friends to the registration page.
    """
    # Arrange
    invitation_link = '/invite/link'

    # Act
    response = client.get(invitation_link, follow_redirects=True)

    # Assert
    assert response.status_code == 200, "Expected status code to be 200 after redirection, got {response.status_code}"
    assert 'Register' in response.text, "Expected registration page content in response"