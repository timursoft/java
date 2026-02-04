@pytest.mark.asyncio
def test_chat_message_delivery_real_time(chat_service):
    """Test that messages are delivered in real-time during gameplay."""
    # Arrange
    sender, receiver = chat_service
    message = "Hello, friend!"
    # Act
    sender.send_message(message)
    received_message = receiver.receive_message(timeout=1)
    # Assert
    assert received_message == message, "Messages should be delivered in real-time"