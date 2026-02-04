@pytest.mark.asyncio
def test_ui_consistent_look_mobile_web(client):
    """Test if the UI looks consistent across mobile and web platforms."""
    response_mobile = client.get("/ui?platform=mobile")
    response_web = client.get("/ui?platform=web")
    assert response_mobile.status_code == 200, "Expected status code 200 for mobile"
    assert response_web.status_code == 200, "Expected status code 200 for web"
    data_mobile = response_mobile.json()
    data_web = response_web.json()
    assert data_mobile['theme'] == data_web['theme'], "Expected themes to be consistent across platforms"