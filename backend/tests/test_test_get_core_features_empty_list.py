def test_get_core_features_empty_list(test_client, mock_no_features):
    """Test response when no core features are available."""
    # Arrange
    response = test_client.get('/api/core-features')

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert 'features' in data, "'features' key missing in response data"
    assert data['features'] == [], "Expected 'features' to be an empty list, got {data['features']}"