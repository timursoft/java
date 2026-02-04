def test_compile_regulations_no_data(mock_regulation_service):
    """
    Test that the regulation service handles no applicable regulations correctly.
    """
    # Arrange
    mock_service = mock_regulation_service
    mock_service.get_applicable_regulations.return_value = []
    
    # Act
    result = compile_regulations(mock_service)
    
    # Assert
    assert result == [], "Expected an empty list when no regulations are applicable"