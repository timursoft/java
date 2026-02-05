def test_visuals_highlight_key_features(mock_visuals, mock_key_features):
    """Test that visuals highlight key features of the app."""
    # Arrange
    visuals = mock_visuals()
    key_features = mock_key_features()

    # Act
    highlighted_features = extract_highlighted_features(visuals)

    # Assert
    assert set(highlighted_features) == set(key_features), "Not all key features are highlighted in visuals."