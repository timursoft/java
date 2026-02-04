def test_app_layout_initialization():
    """Test that the app layout initializes correctly"""
    # Arrange
    app = create_app()
    
    # Act
    response = app.get('/')

    # Assert
    assert response.status_code == 200, "App layout did not initialize correctly."
    assert b'Home' in response.data, "Home page is not in the app layout."