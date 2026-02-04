def test_technical_team_approval_success(mock_approve_framework):
    """
    Test that the technical team approves the selected framework.
    """
    # Arrange
    selected_framework = 'Flutter'

    # Act
    approval_status = mock_approve_framework(selected_framework)

    # Assert
    assert approval_status is True, "Technical team should approve the framework."