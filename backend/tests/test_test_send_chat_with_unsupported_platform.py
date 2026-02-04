def test_send_chat_with_unsupported_platform(test_client):
    """
    Test sending chat message with an unsupported platform.
    """
    # Arrange
    message = "Hello, unsupported platform!"
    platform = "unsupported_platform"

    # Act
    response = test_client.post(f"/api/chat/send?platform={platform}", json={"message": message})

    # Assert
    assert response.status_code == 400, f"Expected status code 400 for unsupported platform, got {response.status_code}"
    assert "error" in response.json(), "Expected error message in response for unsupported platform"