from unittest.mock import patch
import pytest

@pytest.mark.asyncio
def test_email_contains_feedback_link(mock_send_email):
    """
    Test that the email sent to testers contains a link to the feedback form.
    """
    # Arrange
    feedback_link = "http://example.com/feedback"

    # Act
    with patch('email_service.create_feedback_email') as mock_create_email:
        mock_create_email.return_value = f"Please provide feedback: {feedback_link}"
        send_feedback_email_to_testers(60)

    # Assert
    assert feedback_link in mock_create_email.return_value, "Feedback link not present in the email."