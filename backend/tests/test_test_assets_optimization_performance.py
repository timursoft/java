def test_assets_optimization_performance(test_client):
    # Arrange
    response = test_client.post("/create-environment")

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
    assert data['assets']['optimized'], "Assets are not optimized for performance."