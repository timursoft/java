def test_access_emoji_palette_unauthenticated(unauthenticated_client):
    """Test that an unauthenticated player cannot access the emoji palette."""
    response = unauthenticated_client.get("/api/game/emoji_palette")
    assert response.status_code == 401, "Expected 401 Unauthorized when accessing emoji palette without authentication"