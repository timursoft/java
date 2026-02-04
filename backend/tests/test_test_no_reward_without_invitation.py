import pytest
from unittest.mock import patch

@patch('app.rewards_service.credit_reward')
def test_no_reward_without_invitation(mock_credit_reward):
    """
    Test that no reward is given if the friend joins without an invitation link.
    """
    # Arrange
    invitation_link = None
    friend_id = 2
    mock_credit_reward.return_value = False

    # Act
    result = app.process_invitation(invitation_link, friend_id)

    # Assert
    assert result == False, "No reward should be given without an invitation link."
    mock_credit_reward.assert_not_called()