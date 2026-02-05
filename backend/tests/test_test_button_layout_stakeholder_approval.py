def test_button_layout_stakeholder_approval(client: TestClient):
    """
    Test that the new button layout is approved by stakeholders.
    """
    # Arrange
    response = client.get("/api/button-layout/approval-status")
    
    # Act
    approval_data = response.json()
    
    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert 'approval' in approval_data, "Expected 'approval' key in response"
    assert approval_data['approval'] == 'approved', "Expected layout to be 'approved' by stakeholders"