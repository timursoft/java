def test_screenshot_meets_dimensions(screenshot_generator):
    """Test that screenshot meets the required dimensions and format"""
    # Arrange
    required_dimensions = (1080, 1920)
    required_format = 'PNG'
    screenshot = screenshot_generator.generate_screenshot()

    # Act
    screenshot_dimensions = screenshot.get_dimensions()
    screenshot_format = screenshot.get_format()

    # Assert
    assert screenshot_dimensions == required_dimensions, f"Expected dimensions {required_dimensions}, but got {screenshot_dimensions}"
    assert screenshot_format == required_format, f"Expected format {required_format}, but got {screenshot_format}"