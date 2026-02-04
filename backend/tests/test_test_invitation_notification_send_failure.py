def test_invitation_notification_send_failure(client, mocker):
    """Test failure in sending invitation notification due to external service error"""
    # Arrange
    friend_username = "friend123"
    mocker.patch('app.services.notification_service.send_invitation', return_value=False)

    # Act
    response = client.post('/api/invitations/send', json={"username": friend_username})

    # Assert
    assert response.status_code == 500, "Expected status code to be 500 for service error"
    assert response.json() == {"status": "error", "message": "Failed to send invitation"}, "Expected error message for failed invitation notification"