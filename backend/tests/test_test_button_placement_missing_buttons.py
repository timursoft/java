def test_button_placement_missing_buttons(client: TestClient):
    """
    Test handling of missing buttons in the layout response.
    """
    # Arrange
    response = client.get("/api/button-layout")
    
    # Act
    layout_data = response.json()
    
    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert 'buttons' in layout_data, "Expected 'buttons' key in response"
    assert len(layout_data['buttons']) > 0, "Expected at least one button in layout"