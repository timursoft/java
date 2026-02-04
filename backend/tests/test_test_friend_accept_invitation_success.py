def test_friend_accept_invitation_success(client, mocker):
    """Test successful acceptance of invitation by a friend"""
    # Arrange
    invitation_id = "123abc"
    mocker.patch('app.services.invitation_service.accept_invitation', return_value=True)

    # Act
    response = client.post('/api/invitations/accept', json={"invitation_id": invitation_id})

    # Assert
    assert response.status_code == 200, "Expected status code to be 200"
    assert response.json() == {"status": "accepted"}, "Expected accepted status for invitation"