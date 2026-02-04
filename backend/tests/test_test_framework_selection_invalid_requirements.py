def test_framework_selection_invalid_requirements(mock_select_framework):
    """
    Test that an exception is raised when invalid project requirements are provided.
    """
    # Arrange
    invalid_requirements = {'platforms': ['Windows'], 'language': 'Python'}

    # Act & Assert
    with pytest.raises(ValueError, match="No suitable cross-platform framework found"):
        mock_select_framework(invalid_requirements)