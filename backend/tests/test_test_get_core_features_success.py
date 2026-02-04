def test_get_core_features_success(test_client):
    """Test successful retrieval of core features for all platforms."""
    # Arrange
    response = test_client.get('/api/core-features')
    
    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert 'features' in data, "'features' key missing in response data"
    assert isinstance(data['features'], list), "Expected 'features' to be a list, got {type(data['features'])}"
    assert len(data['features']) > 0, "Expected at least one feature, got 0"