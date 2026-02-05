def test_hud_display_time(client):
    response = client.get("/api/hud")
    assert response.status_code == 200, "Expected 200 OK"
    data = response.json()
    assert 'time' in data, "Time information missing in HUD"
    assert isinstance(data['time'], str), "Time should be a string"