def test_confirmation_message_after_post():
    """Test that a confirmation message is displayed after a successful post."""
    # Arrange
    post_result = {'success': True}
    expected_message = "Your score has been successfully shared!"

    # Act
    message = get_confirmation_message(post_result)

    # Assert
    assert message == expected_message, f"Expected '{expected_message}', got '{message}'"