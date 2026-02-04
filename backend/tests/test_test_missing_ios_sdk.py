def test_missing_ios_sdk(mock_ios_sdk):
    """Test configuration failure when iOS SDK is missing."""
    # Arrange
    mock_ios_sdk.install.side_effect = FileNotFoundError("iOS SDK not found")
    # Act & Assert
    with pytest.raises(FileNotFoundError, match="iOS SDK not found"):
        configure_ios_environment()