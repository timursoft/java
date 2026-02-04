from myapp.leaderboard import update_leaderboard
from unittest.mock import Mock

@pytest.fixture
def mock_failed_game_result():
    return {'game_id': 3, 'scores': None}

@pytest.mark.asyncio
def test_leaderboard_update_failure_handling(mock_failed_game_result):
    """
    Test error handling when leaderboard update fails.
    """
    # Arrange
    mock_update_function = Mock(side_effect=Exception("Leaderboard update failed"))

    # Act & Assert
    with pytest.raises(Exception) as excinfo:
        update_leaderboard(mock_failed_game_result)
    assert "Leaderboard update failed" in str(excinfo.value), "Exception not raised as expected."