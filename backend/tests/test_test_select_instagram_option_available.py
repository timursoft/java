def test_select_instagram_option_available(client):
    response = client.get("/api/share/options")
    assert response.status_code == 200, "Failed to retrieve sharing options."
    assert "Instagram" in response.json()["options"], "Instagram option is not available for sharing."