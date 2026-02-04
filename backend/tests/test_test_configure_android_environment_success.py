def test_configure_android_environment_success(mock_android_sdk):
    """Test successful configuration of the Android development environment."""
    # Arrange
    mock_android_sdk.install.return_value = True
    # Act
    result = configure_android_environment()
    # Assert
    assert result is True, "Android environment should be configured successfully"