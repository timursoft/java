def test_invalid_token():
    """Test that requests with an invalid token are rejected."""
    # Arrange
    data = {"share_option": True}
    headers = {"Authorization": "Bearer invalid_token"}

    # Act
    response = client.post("/api/settings/share", json=data, headers=headers)

    # Assert
    assert response.status_code == 401, "Expected status code 401 for invalid token"