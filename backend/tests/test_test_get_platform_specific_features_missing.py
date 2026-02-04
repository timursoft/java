def test_get_platform_specific_features_missing(test_client, mock_all_platforms_features):
    """Test to ensure no platform-specific features are missing from the core features list."""
    # Arrange
    response = test_client.get('/api/core-features')

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert 'features' in data, "'features' key missing in response data"
    expected_features = mock_all_platforms_features
    assert all(feature in data['features'] for feature in expected_features), "Not all expected features are present in the response"