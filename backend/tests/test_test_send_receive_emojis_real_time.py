@pytest.mark.asyncio
def test_send_receive_emojis_real_time(authenticated_client, mock_ws):
    """Test that emojis are sent and received in real-time during gameplay."""
    with mock_ws as ws:
        authenticated_client.websocket_connect("/ws/game")
        ws.send_json({"action": "send_emoji", "emoji": "😊"})
        data = ws.receive_json()
        assert data["action"] == "receive_emoji", "Expected action to be 'receive_emoji'"
        assert data["emoji"] == "😊", "Expected the received emoji to match the sent emoji"