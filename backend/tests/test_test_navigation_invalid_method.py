def test_navigation_invalid_method():
    """Test navigation with invalid method returns error."""
    # Arrange
    app = create_app()
    
    # Act
    response = app.post('/about')

    # Assert
    assert response.status_code == 405, "Invalid method did not return 405."