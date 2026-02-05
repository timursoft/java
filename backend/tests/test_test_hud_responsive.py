@pytest.mark.parametrize("resolution", [(1920, 1080), (1280, 720), (800, 600)])
def test_hud_responsive(client, resolution):
    response = client.get(f"/api/hud?resolution={resolution[0]}x{resolution[1]}")
    assert response.status_code == 200, "Expected 200 OK for resolution"
    data = response.json()
    assert data.get('responsive'), f"HUD not responsive at {resolution}"