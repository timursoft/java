def test_navigation_404_for_invalid_page():
    """Test navigation to a non-existent page returns 404"""
    # Arrange
    app = create_app()
    
    # Act
    response = app.get('/invalid-page')

    # Assert
    assert response.status_code == 404, "Non-existent page did not return 404."