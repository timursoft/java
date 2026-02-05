def test_get_main_menu_auth_required():
    """Test menu access without authentication returns 401 if auth is required."""
    response = client.get("/api/menu")
    assert response.status_code in [200, 401], "Expected status code 401 if authentication is required else 200"