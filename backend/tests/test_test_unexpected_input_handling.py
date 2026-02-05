def test_unexpected_input_handling(client):
    """
    Test the application's ability to handle unexpected inputs after the bug fix.
    """
    # Arrange
    response = client.post("/api/buggy-endpoint", json={"unexpected": "input"})
    # Act
    # Assert
    assert response.status_code == 400, "Expected status code 400 for unexpected input, but got {response.status_code}"
    assert "error" in response.json(), "Expected 'error' in response for unexpected input."