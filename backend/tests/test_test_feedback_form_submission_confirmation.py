def test_feedback_form_submission_confirmation(client):
    """
    Test that a confirmation message is shown after feedback submission.
    """
    # Arrange
    feedback_data = {"text": "This is a test feedback."}
    
    # Act
    response = client.post("/feedback", json=feedback_data)
    
    # Assert
    assert response.status_code == 200, "Feedback submission failed."
    assert "confirmation" in response.json(), "Confirmation message not found in feedback response."