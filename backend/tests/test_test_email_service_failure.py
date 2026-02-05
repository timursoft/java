from unittest.mock import patch
import pytest

@patch('email_service.send_email', side_effect=Exception('Email service failed'))
def test_email_service_failure(mock_send_email):
    """Test email sending when the email service fails."""
    # Arrange
    gameplay_period = 60  # in minutes

    # Act & Assert
    with pytest.raises(Exception, match='Email service failed'):
        trigger_email(gameplay_period)