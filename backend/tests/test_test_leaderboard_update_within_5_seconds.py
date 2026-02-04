import pytest
import time
from unittest.mock import Mock
from myapp.leaderboard import update_leaderboard

@pytest.fixture
def mock_game_result():
    return {'game_id': 1, 'scores': {'user1': 100, 'user2': 200}}

@pytest.fixture
def mock_leaderboard_service(mocker):
    service = mocker.patch('myapp.leaderboard.LeaderboardService')
    return service

@pytest.mark.asyncio
def test_leaderboard_update_within_5_seconds(mock_game_result, mock_leaderboard_service):
    """
    Test that the leaderboard updates within 5 seconds after a game completes.
    """
    # Arrange
    update_leaderboard(mock_game_result)
    
    # Act
    start_time = time.time()
    mock_leaderboard_service.update.assert_called_once_with(mock_game_result)
    elapsed_time = time.time() - start_time

    # Assert
    assert elapsed_time < 5, f"Leaderboard did not update within 5 seconds, took {elapsed_time} seconds."