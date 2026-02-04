from myapp.leaderboard import Leaderboard

@pytest.fixture
def mock_normal_game_result():
    return {'game_id': 4, 'scores': {'user1': 100, 'user2': 150}}

@pytest.mark.asyncio
def test_no_high_score_no_highlight(mock_normal_game_result, mock_leaderboard):
    """
    Test that no highlight occurs if there is no new high score.
    """
    # Arrange
    leaderboard = Leaderboard()
    mock_leaderboard.highlight_high_scores.return_value = False

    # Act
    highlight_result = leaderboard.highlight_high_scores(mock_normal_game_result)

    # Assert
    assert not highlight_result, "Highlight occurred despite no new high score."