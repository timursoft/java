@pytest.mark.asyncio
def test_ui_adapts_screen_size_web(client):
    """Test if the UI adapts to a standard web screen size."""
    response = client.get("/ui?platform=web")
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'layout' in data, "Expected 'layout' in response"
    assert data['layout'] == 'web', "Expected layout to be 'web'"