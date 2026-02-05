from unittest.mock import patch

@patch('email_service.send_email')
def test_email_sent_after_gameplay_period(mock_send_email):
    """Test that an email is sent to the tester after the specified gameplay period."""
    # Arrange
    gameplay_period = 60  # in minutes

    # Act
    trigger_email(gameplay_period)

    # Assert
    mock_send_email.assert_called_once_with('tester@example.com', 'Feedback Request')