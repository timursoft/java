@pytest.mark.asyncio
def test_ui_adapts_screen_size_mobile(client):
    """Test if the UI adapts to a standard mobile screen size."""
    response = client.get("/ui?platform=mobile")
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'layout' in data, "Expected 'layout' in response"
    assert data['layout'] == 'mobile', "Expected layout to be 'mobile'"