def test_confirmation_message_after_failed_post():
    """Test that a failure message is displayed after an unsuccessful post."""
    # Arrange
    post_result = {'success': False}
    expected_message = "There was an error sharing your score. Please try again."

    # Act
    message = get_confirmation_message(post_result)

    # Assert
    assert message == expected_message, f"Expected '{expected_message}', got '{message}'"