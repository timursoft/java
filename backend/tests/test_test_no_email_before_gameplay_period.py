from unittest.mock import patch

@patch('email_service.send_email')
def test_no_email_before_gameplay_period(mock_send_email):
    """Test that no email is sent if the gameplay period is not reached."""
    # Arrange
    gameplay_period = 30  # in minutes

    # Act
    trigger_email(gameplay_period)

    # Assert
    mock_send_email.assert_not_called()