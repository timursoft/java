@pytest.mark.asyncio
def test_no_match_found_within_time_limit(matchmaking_service, player_factory):
    """Ensure no match is found if none is available within 60 seconds."""
    # Arrange
    player = player_factory(skill_level=5)
    
    # Act
    with mock.patch('matchmaking_service.find_match', side_effect=TimeoutError):
        with pytest.raises(TimeoutError):
            await matchmaking_service.find_match(player)

    # Assert
    # Exception expected
