def test_create_environment_includes_lighting(test_client):
    # Arrange
    response = test_client.post("/create-environment")

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
    assert 'lighting' in data['environment'], "Lighting not included in environment creation."