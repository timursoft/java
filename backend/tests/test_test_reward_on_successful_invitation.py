import pytest
from unittest.mock import patch

@patch('app.rewards_service.credit_reward')
def test_reward_on_successful_invitation(mock_credit_reward):
    """
    Test that a user receives a reward when a friend joins using their invitation link.
    """
    # Arrange
    invitation_link = 'http://game.com/invite?code=12345'
    user_id = 1
    friend_id = 2
    mock_credit_reward.return_value = True

    # Act
    result = app.process_invitation(invitation_link, friend_id)

    # Assert
    assert result == True, "User should receive a reward for successful invitation."
    mock_credit_reward.assert_called_once_with(user_id)