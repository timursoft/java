def test_visuals_approval_by_marketing_team(mock_visuals, mock_marketing_team):
    """Test that visuals are approved by the marketing team."""
    # Arrange
    visuals = mock_visuals()
    marketing_team = mock_marketing_team()

    # Act
    approval_status = marketing_team.approve_visuals(visuals)

    # Assert
    assert approval_status, "Visuals are not approved by the marketing team."