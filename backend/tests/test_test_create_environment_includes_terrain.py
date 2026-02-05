def test_create_environment_includes_terrain(test_client):
    # Arrange
    response = test_client.post("/create-environment")

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
    assert 'terrain' in data['environment'], "Terrain not included in environment creation."