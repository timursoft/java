def test_framework_selection_edge_case_no_language(mock_select_framework):
    """
    Test framework selection when no programming language is specified.
    """
    # Arrange
    incomplete_requirements = {'platforms': ['iOS', 'Android']}
    expected_framework = 'React Native'

    # Act
    selected_framework = mock_select_framework(incomplete_requirements)

    # Assert
    assert selected_framework == expected_framework, f"Expected {expected_framework} when no language specified, but got {selected_framework}"