def test_feedback_form_text_input(client):
    """
    Test that the feedback form allows text input.
    """
    # Arrange
    feedback_data = {"text": "This is a test feedback."}
    
    # Act
    response = client.post("/feedback", json=feedback_data)
    
    # Assert
    assert response.status_code == 200, "Feedback submission failed."
    assert response.json().get("message") == "Feedback submitted successfully.", "Feedback submission message is incorrect."