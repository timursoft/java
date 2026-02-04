def test_successful_confirmation_message_after_sharing(client, mock_instagram_api):
    mock_instagram_api.send.return_value = True
    response = client.post("/api/share", json={"platform": "Instagram", "data": {"rank": 1, "name": "John Doe", "score": 100}})
    assert response.status_code == 200, "Sharing on Instagram failed."
    assert response.json()["message"] == "Successfully shared on Instagram!", "Incorrect confirmation message after sharing."