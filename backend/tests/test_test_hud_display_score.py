def test_hud_display_score(client):
    response = client.get("/api/hud")
    assert response.status_code == 200, "Expected 200 OK"
    data = response.json()
    assert 'score' in data, "Score information missing in HUD"
    assert isinstance(data['score'], int), "Score should be an integer"