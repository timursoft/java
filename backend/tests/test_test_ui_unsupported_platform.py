@pytest.mark.asyncio
def test_ui_unsupported_platform(client):
    """Test the response when an unsupported platform is requested."""
    response = client.get("/ui?platform=tablet")
    assert response.status_code == 404, "Expected status code 404 for unsupported platform"