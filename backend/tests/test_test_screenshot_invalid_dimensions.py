def test_screenshot_invalid_dimensions(screenshot_generator):
    """Test that an error is raised for invalid screenshot dimensions"""
    # Arrange
    invalid_dimensions = (500, 500)
    screenshot_generator.set_dimensions(invalid_dimensions)

    # Act and Assert
    with pytest.raises(ValueError, match="Invalid screenshot dimensions"):
        screenshot_generator.generate_screenshot()