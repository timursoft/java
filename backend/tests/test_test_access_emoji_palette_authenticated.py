def test_access_emoji_palette_authenticated(authenticated_client):
    """Test that an authenticated player can access the emoji palette during gameplay."""
    response = authenticated_client.get("/api/game/emoji_palette")
    assert response.status_code == 200, "Expected 200 OK when accessing emoji palette as authenticated player"
    assert 'emojis' in response.json(), "Response should contain 'emojis' key with available emojis"