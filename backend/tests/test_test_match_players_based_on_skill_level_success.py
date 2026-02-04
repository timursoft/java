@pytest.mark.asyncio
def test_match_players_based_on_skill_level_success(matchmaking_service, player_factory):
    """Ensure players are matched based on skill level."""
    # Arrange
    player_1 = player_factory(skill_level=5)
    player_2 = player_factory(skill_level=5)
    
    # Act
    match = await matchmaking_service.find_match(player_1)

    # Assert
    assert match.opponent == player_2, "Players with the same skill level should be matched."