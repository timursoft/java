import pytest
from unittest.mock import patch

@patch('app.database.update_user_account')
@patch('app.rewards_service.credit_reward')
def test_reward_credited_to_user_account(mock_credit_reward, mock_update_user_account):
    """
    Test that the reward is credited to the user's account after a successful invitation.
    """
    # Arrange
    user_id = 1
    friend_id = 2
    reward_amount = 100
    mock_credit_reward.return_value = reward_amount

    # Act
    app.process_invitation('http://game.com/invite?code=12345', friend_id)

    # Assert
    mock_update_user_account.assert_called_once_with(user_id, reward_amount)