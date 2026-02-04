def test_friend_accept_invitation_failure(client, mocker):
    """Test failure in accepting an expired invitation by a friend"""
    # Arrange
    invitation_id = "expired123"
    mocker.patch('app.services.invitation_service.accept_invitation', return_value=False)

    # Act
    response = client.post('/api/invitations/accept', json={"invitation_id": invitation_id})

    # Assert
    assert response.status_code == 400, "Expected status code to be 400 for expired invitation"
    assert response.json() == {"status": "error", "message": "Invitation expired"}, "Expected error message for expired invitation"