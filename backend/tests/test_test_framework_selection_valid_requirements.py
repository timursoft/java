def test_framework_selection_valid_requirements(mock_select_framework):
    """
    Test that a valid framework is selected based on project requirements.
    """
    # Arrange
    project_requirements = {'platforms': ['iOS', 'Android'], 'language': 'Dart'}
    expected_framework = 'Flutter'

    # Act
    selected_framework = mock_select_framework(project_requirements)

    # Assert
    assert selected_framework == expected_framework, f"Expected {expected_framework}, but got {selected_framework}"