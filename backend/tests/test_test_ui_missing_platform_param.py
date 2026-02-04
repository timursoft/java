@pytest.mark.asyncio
def test_ui_missing_platform_param(client):
    """Test the response when the 'platform' query parameter is missing."""
    response = client.get("/ui")
    assert response.status_code == 400, "Expected status code 400 when platform is missing"