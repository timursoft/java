def test_invalid_emoji_handling(authenticated_client):
    """Test handling of invalid emoji input during gameplay."""
    response = authenticated_client.post("/api/game/send_emoji", json={"emoji": "invalid_emoji"})
    assert response.status_code == 400, "Expected 400 Bad Request when sending an invalid emoji"