def test_friend_decline_invitation_success(client, mocker):
    """Test successful decline of invitation by a friend"""
    # Arrange
    invitation_id = "123abc"
    mocker.patch('app.services.invitation_service.decline_invitation', return_value=True)

    # Act
    response = client.post('/api/invitations/decline', json={"invitation_id": invitation_id})

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == {"status": "declined"}, "Expected declined status for invitation"