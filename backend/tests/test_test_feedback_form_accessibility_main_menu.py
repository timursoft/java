def test_feedback_form_accessibility_main_menu(client):
    """
    Test that the feedback form is accessible from the main menu.
    """
    # Arrange
    response = client.get("/main-menu")
    
    # Act
    assert response.status_code == 200, "Main menu is not accessible."
    
    # Act
    form_link = response.json().get("feedback_form_link")
    
    # Assert
    assert form_link is not None, "Feedback form link is not available in the main menu."