@pytest.mark.asyncio
def test_delayed_message_delivery_under_high_latency(chat_service, simulate_high_latency):
    """Test message delivery under high latency conditions."""
    # Arrange
    sender, receiver = chat_service
    simulate_high_latency()
    message = "Hello, friend!"
    # Act
    sender.send_message(message)
    received_message = receiver.receive_message(timeout=5)
    # Assert
    assert received_message == message, "Messages should eventually be delivered under high latency"