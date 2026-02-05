def test_visuals_not_highlight_irrelevant_features(mock_visuals, mock_irrelevant_features):
    """Test that visuals do not highlight irrelevant features."""
    # Arrange
    visuals = mock_visuals()
    irrelevant_features = mock_irrelevant_features()

    # Act
    highlighted_features = extract_highlighted_features(visuals)

    # Assert
    assert not any(feature in highlighted_features for feature in irrelevant_features), "Visuals incorrectly highlight irrelevant features."