def test_get_main_menu_layout_consistency():
    """Test the consistency of the menu layout with design guidelines."""
    response = client.get("/api/menu/layout")
    assert response.status_code == 200, "Expected status code 200"
    layout_guidelines = {"layout": "consistent"}
    assert response.json() == layout_guidelines, "Menu layout does not match design guidelines"