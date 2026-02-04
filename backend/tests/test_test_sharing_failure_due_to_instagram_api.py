def test_sharing_failure_due_to_instagram_api(client, mock_instagram_api):
    mock_instagram_api.send.return_value = False
    response = client.post("/api/share", json={"platform": "Instagram", "data": {"rank": 1, "name": "John Doe", "score": 100}})
    assert response.status_code == 503, "Expected 503 Service Unavailable due to Instagram API failure."
    assert "message" in response.json(), "Error message not found for Instagram API failure."