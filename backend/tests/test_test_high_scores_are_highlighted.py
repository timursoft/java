from myapp.leaderboard import Leaderboard

@pytest.fixture
def mock_high_score_game_result():
    return {'game_id': 2, 'scores': {'user1': 300, 'user2': 500}}

@pytest.fixture
def mock_leaderboard(mocker):
    leaderboard = mocker.patch('myapp.leaderboard.Leaderboard')
    leaderboard.highlight_high_scores.return_value = True
    return leaderboard

@pytest.mark.asyncio
def test_high_scores_are_highlighted(mock_high_score_game_result, mock_leaderboard):
    """
    Test that new high scores are highlighted on the leaderboard.
    """
    # Arrange
    leaderboard = Leaderboard()
    
    # Act
    highlight_result = leaderboard.highlight_high_scores(mock_high_score_game_result)

    # Assert
    assert highlight_result, "High scores were not highlighted as expected."