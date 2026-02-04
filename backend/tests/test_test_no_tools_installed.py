def test_no_tools_installed(mock_tools_installer):
    """Test environment setup failure when no tools are installed."""
    # Arrange
    mock_tools_installer.install_all.side_effect = InstallationError("No tools installed")
    # Act & Assert
    with pytest.raises(InstallationError, match="No tools installed"):
        configure_all_tools()