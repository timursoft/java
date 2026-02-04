def test_emoji_displayed_correctly_in_chat(authenticated_client, db_session):
    """Test that selected emojis are displayed correctly in the game chat."""
    response = authenticated_client.post("/api/game/send_emoji", json={"emoji": "😊"})
    assert response.status_code == 200, "Expected 200 OK when sending emoji"
    chat_messages = db_session.query(ChatMessage).filter(ChatMessage.emoji == "😊").all()
    assert len(chat_messages) > 0, "Expected to find chat messages with the emoji '😊'"