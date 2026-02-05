def test_screenshot_format_edge_case(screenshot_generator):
    """Test edge case for unsupported screenshot format"""
    # Arrange
    unsupported_format = 'TIFF'
    screenshot_generator.set_format(unsupported_format)

    # Act and Assert
    with pytest.raises(ValueError, match="Unsupported screenshot format"):
        screenshot_generator.generate_screenshot()