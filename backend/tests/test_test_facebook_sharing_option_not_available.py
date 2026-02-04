def test_facebook_sharing_option_not_available(test_client, mock_service_down):
    """Test that the Facebook option is not available when the service is down."""
    # Arrange
    mock_service_down.return_value = False
    # Act
    response = test_client.get("/share/options")
    sharing_options = response.json()
    # Assert
    assert "facebook" not in sharing_options, "Facebook option should not be available when service is down"