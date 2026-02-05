def test_hud_display_health(client):
    response = client.get("/api/hud")
    assert response.status_code == 200, "Expected 200 OK"
    data = response.json()
    assert 'health' in data, "Health information missing in HUD"
    assert isinstance(data['health'], int), "Health should be an integer"