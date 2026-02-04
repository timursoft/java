from myapp.notifications import notify_users_of_ranking
from unittest.mock import patch

@pytest.fixture
def mock_user_rankings():
    return {'user1': 1, 'user2': 2}

@pytest.mark.asyncio
def test_users_notified_of_ranking(mock_user_rankings):
    """
    Test that users are notified of their ranking after the leaderboard update.
    """
    # Arrange
    with patch('myapp.notifications.notify_users_of_ranking') as mock_notify:
        
        # Act
        notify_users_of_ranking(mock_user_rankings)

        # Assert
        mock_notify.assert_called_once_with(mock_user_rankings)
        assert mock_notify.call_count == 1, "Users were not notified of their ranking as expected."