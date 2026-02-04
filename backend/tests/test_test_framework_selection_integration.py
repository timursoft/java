@pytest.mark.asyncio
def test_framework_selection_integration(async_mock_select_and_approve_framework):
    """
    Integration test to verify the complete flow of framework selection and approval.
    """
    # Arrange
    project_requirements = {'platforms': ['iOS', 'Android'], 'language': 'Dart'}

    # Act
    approval_status, selected_framework = await async_mock_select_and_approve_framework(project_requirements)

    # Assert
    assert approval_status is True, "The approval status should be true for a valid framework."
    assert selected_framework == 'Flutter', f"Expected framework to be 'Flutter', but got {selected_framework}."