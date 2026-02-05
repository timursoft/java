import pytest

@pytest.mark.asyncio
def test_feedback_form_rejects_empty_text(client):
    """
    Test that the feedback form rejects empty text input.
    """
    # Arrange
    feedback_text = ""
    feedback_url = "/feedback"

    # Act
    response = client.post(feedback_url, json={"text": feedback_text})

    # Assert
    assert response.status_code == 400, "Feedback form accepted empty text input."