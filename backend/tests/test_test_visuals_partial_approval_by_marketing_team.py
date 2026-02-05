def test_visuals_partial_approval_by_marketing_team(mock_partial_approval_visuals, mock_marketing_team):
    """Test edge case where only some visuals are approved by the marketing team."""
    # Arrange
    visuals = mock_partial_approval_visuals()
    marketing_team = mock_marketing_team()

    # Act
    approved_visuals = marketing_team.approve_visuals(visuals)

    # Assert
    assert len(approved_visuals) < len(visuals), "All visuals were approved, expected partial approval."