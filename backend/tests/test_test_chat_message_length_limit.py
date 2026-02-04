def test_chat_message_length_limit(test_client):
    """
    Test that chat message length does not exceed platform limits.
    """
    # Arrange
    message = "x" * 500  # assuming 500 is the maximum length allowed
    platform = "pc"

    # Act
    response = test_client.post(f"/api/chat/send?platform={platform}", json={"message": message})

    # Assert
    assert response.status_code == 200, f"Expected status code 200 for message within length limit, got {response.status_code}"
    assert response.json()["message"] == message, "Expected message to be sent successfully"