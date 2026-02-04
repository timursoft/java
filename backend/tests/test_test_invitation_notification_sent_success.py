def test_invitation_notification_sent_success(client, mocker):
    """Test successful sending of invitation notification to a friend"""
    # Arrange
    friend_username = "friend123"
    mocker.patch('app.services.notification_service.send_invitation', return_value=True)

    # Act
    response = client.post('/api/invitations/send', json={"username": friend_username})

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == {"status": "success"}, "Expected success status for invitation notification"