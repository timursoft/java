@pytest.mark.asyncio
def test_notification_sent_when_match_found(matchmaking_service, player_factory, notification_service):
    """Ensure notification is sent when match is found."""
    # Arrange
    player = player_factory(skill_level=5)
    
    # Act
    match = await matchmaking_service.find_match(player)
    notification_service.send_notification.assert_called_once_with(player, match.opponent)

    # Assert
    assert notification_service.send_notification.called, "Notification should be sent when a match is found."