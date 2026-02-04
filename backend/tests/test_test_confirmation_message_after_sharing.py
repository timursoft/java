def test_confirmation_message_after_sharing(test_client, mocker):
    """Test that a confirmation message is shown after successfully sharing on Twitter."""
    # Arrange
    mocker.patch('twitter_api.share', return_value=True)
    response = test_client.post('/api/share/twitter', json={'ranking': '1st'})
    # Act
    confirmation_message = response.json().get('message')
    # Assert
    assert confirmation_message == "Successfully shared on Twitter!", "Confirmation message should indicate successful sharing."