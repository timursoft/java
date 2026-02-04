def test_navigation_home_to_about():
    """Test navigation from Home to About page."""
    # Arrange
    app = create_app()
    
    # Act
    response = app.get('/about')

    # Assert
    assert response.status_code == 200, "Navigation to About page failed."