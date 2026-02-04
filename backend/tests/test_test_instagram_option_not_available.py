def test_instagram_option_not_available(client):
    response = client.get("/api/share/options?enabled=false")
    assert response.status_code == 200, "Failed to retrieve sharing options when disabled."
    assert "Instagram" not in response.json()["options"], "Instagram option should not be available when sharing is disabled."