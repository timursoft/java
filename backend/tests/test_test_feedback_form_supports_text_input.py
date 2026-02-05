def test_feedback_form_supports_text_input():
    """Test that the feedback form allows text input."""
    # Arrange
    feedback_form = get_feedback_form()

    # Act
    supports_text = feedback_form.supports_text_input()

    # Assert
    assert supports_text, 'Feedback form does not support text input'