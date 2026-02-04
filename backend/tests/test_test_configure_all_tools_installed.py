def test_configure_all_tools_installed(mock_tools_installer):
    """Test that all necessary tools are installed during environment setup."""
    # Arrange
    mock_tools_installer.install_all.return_value = True
    # Act
    result = configure_all_tools()
    # Assert
    assert result is True, "All necessary tools should be installed successfully"