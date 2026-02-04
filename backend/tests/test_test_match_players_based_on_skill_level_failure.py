@pytest.mark.asyncio
def test_match_players_based_on_skill_level_failure(matchmaking_service, player_factory):
    """Ensure players are not matched if skill levels differ significantly."""
    # Arrange
    player_1 = player_factory(skill_level=1)
    player_2 = player_factory(skill_level=10)
    
    # Act
    match = await matchmaking_service.find_match(player_1)

    # Assert
    assert match is None, "Players with vastly different skill levels should not be matched."