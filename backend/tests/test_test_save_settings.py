def test_save_settings():
    """Test that settings are saved and applied correctly."""
    # Arrange
    data = {
        "share_option": True,
        "platforms": ["facebook", "twitter"]
    }
    headers = {"Authorization": "Bearer valid_token"}

    # Act
    response = client.post("/api/settings/save", json=data, headers=headers)

    # Assert
    assert response.status_code == 200, "Expected status code 200 for saving settings"
    assert response.json()["success"] is True, "Expected success to be True when saving settings"