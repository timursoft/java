def test_leaderboard_format_for_instagram(client, leaderboard_data):
    response = client.post("/api/share/format", json={"platform": "Instagram", "data": leaderboard_data})
    assert response.status_code == 200, "Failed to format leaderboard for Instagram."
    assert response.json()["format"] == "formatted_instagram_style", "Leaderboard format is incorrect for Instagram."