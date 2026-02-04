def test_get_core_features_unauthorized(test_client):
    """Test unauthorized access to core features endpoint."""
    # Arrange
    response = test_client.get('/api/core-features', headers={"Authorization": "Bearer invalid_token"})

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 401, "Expected status code 401 for unauthorized access, got {response.status_code}"
    assert 'detail' in data, "Expected 'detail' in response data for error message"