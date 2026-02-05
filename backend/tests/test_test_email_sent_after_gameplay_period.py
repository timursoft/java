from unittest.mock import patch
import pytest

@pytest.mark.asyncio
def test_email_sent_after_gameplay_period(mock_send_email):
    """
    Test that an email is sent to testers after a certain gameplay period.
    """
    # Arrange
    gameplay_period = 60  # 60 minutes
    expected_email_count = 1

    # Act
    with patch('email_service.send_email') as mock_send_email:
        send_feedback_email_to_testers(gameplay_period)

    # Assert
    assert mock_send_email.call_count == expected_email_count, "Email was not sent after the gameplay period."