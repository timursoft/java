def test_compile_regulations_server_error(mock_regulation_service):
    """
    Test that the regulation service handles server errors gracefully.
    """
    # Arrange
    mock_service = mock_regulation_service
    mock_service.get_applicable_regulations.side_effect = Exception("Server Error")
    
    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        compile_regulations(mock_service)
    assert str(exc_info.value) == "Server Error", "Did not handle server error as expected"