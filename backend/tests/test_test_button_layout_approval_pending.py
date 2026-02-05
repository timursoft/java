def test_button_layout_approval_pending(client: TestClient):
    """
    Test edge case where the button layout is pending approval.
    """
    # Arrange
    response = client.get("/api/button-layout/approval-status")
    
    # Act
    approval_data = response.json()
    
    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert 'approval' in approval_data, "Expected 'approval' key in response"
    assert approval_data['approval'] == 'pending', "Expected layout approval status to be 'pending'"