def test_feedback_form_screenshot_attachment(client):
    """
    Test that the feedback form allows optional screenshot attachment.
    """
    # Arrange
    feedback_data = {
        "text": "This is a test feedback.",
        "screenshot": "mock_screenshot_data"
    }
    
    # Act
    response = client.post("/feedback", json=feedback_data)
    
    # Assert
    assert response.status_code == 200, "Feedback submission with screenshot failed."
    assert response.json().get("message") == "Feedback submitted successfully.", "Feedback submission message with screenshot is incorrect."