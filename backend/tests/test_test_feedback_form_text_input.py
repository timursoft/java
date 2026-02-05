import pytest

@pytest.mark.asyncio
def test_feedback_form_text_input(client):
    """
    Test that the feedback form supports text input.
    """
    # Arrange
    feedback_text = "This is a test feedback."
    feedback_url = "/feedback"

    # Act
    response = client.post(feedback_url, json={"text": feedback_text})

    # Assert
    assert response.status_code == 200, "Feedback form did not accept text input."
    assert response.json().get('message') == 'Feedback submitted successfully.', "Feedback was not submitted successfully."