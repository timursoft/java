def test_preferred_social_media_platforms():
    """Test user can choose preferred social media platforms."""
    # Arrange
    data = {"platforms": ["facebook", "twitter"]}
    headers = {"Authorization": "Bearer valid_token"}

    # Act
    response = client.post("/api/settings/platforms", json=data, headers=headers)

    # Assert
    assert response.status_code == 200, "Expected status code 200 for setting platforms"
    assert response.json()["success"] is True, "Expected success to be True when setting platforms"