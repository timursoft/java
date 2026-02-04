def test_select_facebook_sharing_option(test_client):
    """Test that the Facebook sharing option can be selected by the user."""
    # Arrange
    response = test_client.get("/share/options")
    # Act
    sharing_options = response.json()
    # Assert
    assert "facebook" in sharing_options, "Facebook option should be available for sharing"