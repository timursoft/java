from unittest.mock import patch
import pytest

@pytest.mark.asyncio
def test_no_email_sent_before_gameplay_period(mock_send_email):
    """
    Test that no email is sent before the gameplay period has elapsed.
    """
    # Arrange
    gameplay_period = 30  # Less than required
    expected_email_count = 0

    # Act
    with patch('email_service.send_email') as mock_send_email:
        send_feedback_email_to_testers(gameplay_period)

    # Assert
    assert mock_send_email.call_count == expected_email_count, "Email was sent before the gameplay period elapsed."