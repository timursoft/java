def test_app_layout_missing_elements():
    """Test app layout with missing elements."""
    # Arrange
    app = create_app()
    
    # Act
    response = app.get('/')

    # Assert
    assert b'Home' not in response.data, "App layout should not have Home when elements are missing."