def test_chat_message_consistency_pc_mobile_console(test_client):
    """
    Test that chat messages appear the same on PC, mobile, and console.
    """
    # Arrange
    message = "Hello, world! 🌍"
    platforms = ["pc", "mobile", "console"]

    # Act & Assert
    for platform in platforms:
        response = test_client.post(f"/api/chat/send?platform={platform}", json={"message": message})
        assert response.status_code == 200, f"Expected status code 200 for platform {platform}, got {response.status_code}"
        assert response.json()["message"] == message, f"Expected message to be consistent on {platform}, got {response.json()['message']}"