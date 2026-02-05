def test_button_placement_intuitive_locations(client: TestClient):
    """
    Test that buttons are placed in intuitive locations as per the new design.
    """
    # Arrange
    response = client.get("/api/button-layout")
    
    # Act
    layout_data = response.json()
    
    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert 'buttons' in layout_data, "Expected 'buttons' key in response"
    assert layout_data['buttons'] == ['save', 'cancel', 'edit'], "Expected buttons to be in ['save', 'cancel', 'edit'] order"