def test_leaderboard_format_missing_data(client):
    response = client.post("/api/share/format", json={"platform": "Instagram"})
    assert response.status_code == 400, "Expected error for missing leaderboard data, but got a different status."
    assert "error" in response.json(), "Error message not found when leaderboard data is missing."