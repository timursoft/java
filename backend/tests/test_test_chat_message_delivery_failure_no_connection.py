@pytest.mark.asyncio
def test_chat_message_delivery_failure_no_connection(chat_service, disconnect_network):
    """Test that messages are not delivered when there is no network connection."""
    # Arrange
    sender, _ = chat_service
    disconnect_network()
    message = "Hello, friend!"
    # Act & Assert
    with pytest.raises(ConnectionError, match="No connection"):
        sender.send_message(message)