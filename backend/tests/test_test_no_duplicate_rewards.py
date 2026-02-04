import pytest
from unittest.mock import patch

@patch('app.rewards_service.credit_reward')
def test_no_duplicate_rewards(mock_credit_reward):
    """
    Test that no duplicate rewards are credited for the same invitation link.
    """
    # Arrange
    invitation_link = 'http://game.com/invite?code=12345'
    friend_id = 2
    mock_credit_reward.return_value = True

    # Act
    app.process_invitation(invitation_link, friend_id)
    result = app.process_invitation(invitation_link, friend_id)  # Attempt to process again

    # Assert
    assert result == False, "No duplicate rewards should be given for the same invitation."
    mock_credit_reward.assert_called_once()