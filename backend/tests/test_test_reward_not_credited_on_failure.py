import pytest
from unittest.mock import patch

@patch('app.rewards_service.credit_reward', side_effect=Exception('Crediting failed'))
def test_reward_not_credited_on_failure(mock_credit_reward):
    """
    Test that rewards are not credited to the user's account if the crediting process fails.
    """
    # Arrange
    invitation_link = 'http://game.com/invite?code=12345'
    friend_id = 2
    
    # Act & Assert
    with pytest.raises(Exception, match='Crediting failed'):
        app.process_invitation(invitation_link, friend_id)