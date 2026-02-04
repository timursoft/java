def test_missing_android_sdk(mock_android_sdk):
    """Test configuration failure when Android SDK is missing."""
    # Arrange
    mock_android_sdk.install.side_effect = FileNotFoundError("Android SDK not found")
    # Act & Assert
    with pytest.raises(FileNotFoundError, match="Android SDK not found"):
        configure_android_environment()