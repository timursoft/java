def test_emoji_consistency_across_platforms(test_client):
    """
    Test that emojis appear the same across all supported platforms.
    """
    # Arrange
    emoji = "😊"
    platforms = ["pc", "mobile", "console"]

    # Act & Assert
    for platform in platforms:
        response = test_client.post(f"/api/chat/send?platform={platform}", json={"message": emoji})
        assert response.status_code == 200, f"Expected status code 200 for platform {platform}, got {response.status_code}"
        assert response.json()["message"] == emoji, f"Expected emoji to be consistent on {platform}, got {response.json()['message']}"