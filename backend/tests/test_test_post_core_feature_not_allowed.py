def test_post_core_feature_not_allowed(test_client):
    """Test that POST requests to core features endpoint are not allowed."""
    # Arrange
    response = test_client.post('/api/core-features', json={"feature": "new feature"})

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 405, "Expected status code 405 for method not allowed, got {response.status_code}"
    assert 'detail' in data, "Expected 'detail' in response data for error message"