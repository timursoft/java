def test_partial_tool_installation_failure(mock_tools_installer):
    """Test environment setup when some tools fail to install."""
    # Arrange
    mock_tools_installer.install_all.side_effect = PartialInstallationError("Some tools failed to install")
    # Act & Assert
    with pytest.raises(PartialInstallationError, match="Some tools failed to install"):
        configure_all_tools()