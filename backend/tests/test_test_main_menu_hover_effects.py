def test_main_menu_hover_effects():
    """Test hover effects for menu buttons."""
    response = client.get("/api/menu/effects")
    assert response.status_code == 200, "Expected status code 200"
    effects = {"hover": "enabled", "animation": "enabled"}
    assert response.json() == effects, "Hover effects or animations not implemented correctly"