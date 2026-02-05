def test_feedback_form_invalid_data(client):
    """
    Test feedback form submission with invalid data.
    """
    # Arrange
    feedback_data = {"text": "", "screenshot": "invalid_data"}
    
    # Act
    response = client.post("/feedback", json=feedback_data)
    
    # Assert
    assert response.status_code == 400, "Invalid feedback data should result in a 400 status code."
    assert "error" in response.json(), "Error message should be present for invalid feedback data submission."