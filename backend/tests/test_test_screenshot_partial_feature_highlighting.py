def test_screenshot_partial_feature_highlighting(screenshot_generator, partial_features):
    """Test that partial features are not highlighted incorrectly"""
    # Arrange
    screenshot = screenshot_generator.generate_screenshot()

    # Act
    highlighted_features = screenshot.get_highlighted_features()

    # Assert
    for feature in partial_features:
        assert feature not in highlighted_features, f"Partial feature {feature} should not be highlighted"