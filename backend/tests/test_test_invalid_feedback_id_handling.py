def test_invalid_feedback_id_handling(client: TestClient):
    """
    Test handling of an invalid feedback ID when requesting button layout feedback.
    """
    # Arrange
    invalid_feedback_id = 9999
    response = client.get(f"/api/button-layout/feedback/{invalid_feedback_id}")
    
    # Act
    
    # Assert
    assert response.status_code == 404, "Expected status code 404 for invalid feedback ID"