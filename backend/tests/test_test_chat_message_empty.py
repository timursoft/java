def test_chat_message_empty(test_client):
    """
    Test sending an empty chat message.
    """
    # Arrange
    message = ""
    platform = "pc"

    # Act
    response = test_client.post(f"/api/chat/send?platform={platform}", json={"message": message})

    # Assert
    assert response.status_code == 400, "Expected status code 400 for empty message, got {response.status_code}"
    assert "error" in response.json(), "Expected error message for empty message"