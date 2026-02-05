def test_get_main_menu_invalid_endpoint():
    """Test non-existent menu endpoint returns 404 error."""
    response = client.get("/api/menu/nonexistent")
    assert response.status_code == 404, "Expected status code 404 for nonexistent endpoint"