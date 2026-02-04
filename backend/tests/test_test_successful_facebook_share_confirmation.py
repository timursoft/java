def test_successful_facebook_share_confirmation(test_client, mock_facebook_api):
    """Test that a successful confirmation message is received after sharing on Facebook."""
    # Arrange
    mock_facebook_api.post.return_value = {
        "status": "success",
        "message": "Shared successfully on Facebook"
    }
    # Act
    response = test_client.post("/share/facebook", json={"rank": 1, "user": "test_user", "score": 1500})
    # Assert
    assert response.json()["message"] == "Shared successfully on Facebook", "Confirmation message should indicate success"