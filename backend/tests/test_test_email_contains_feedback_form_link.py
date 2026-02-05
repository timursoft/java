def test_email_contains_feedback_form_link():
    """Test that the email contains a link to the feedback form."""
    # Arrange
    email_content = generate_email_content()

    # Act
    link_present = 'http://feedback-form.com' in email_content

    # Assert
    assert link_present, 'Email does not contain feedback form link'