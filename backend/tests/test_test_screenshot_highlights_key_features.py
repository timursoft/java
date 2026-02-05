def test_screenshot_highlights_key_features(screenshot_generator, key_features):
    """Test that screenshot highlights key app features"""
    # Arrange
    screenshot = screenshot_generator.generate_screenshot()

    # Act
    highlighted_features = screenshot.get_highlighted_features()

    # Assert
    for feature in key_features:
        assert feature in highlighted_features, f"Feature {feature} is not highlighted"