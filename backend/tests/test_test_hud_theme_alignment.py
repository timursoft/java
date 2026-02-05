def test_hud_theme_alignment(client):
    response = client.get("/api/hud")
    assert response.status_code == 200, "Expected 200 OK"
    data = response.json()
    assert data.get('theme') == 'expected_theme', "HUD theme does not align with expected game theme"