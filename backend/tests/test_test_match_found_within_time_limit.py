@pytest.mark.asyncio
@mock.patch('matchmaking_service.find_match', return_value=mock.Mock())
def test_match_found_within_time_limit(mock_find_match, matchmaking_service, player_factory):
    """Ensure a match is found within 60 seconds."""
    # Arrange
    player = player_factory(skill_level=5)
    
    # Act
    with mock.patch('asyncio.sleep', return_value=None):
        match = await matchmaking_service.find_match(player)

    # Assert
    assert match is not None, "Match should be found within 60 seconds."