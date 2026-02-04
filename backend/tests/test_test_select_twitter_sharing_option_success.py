def test_select_twitter_sharing_option_success(test_client):
    """Test that a user can successfully select Twitter as a sharing option."""
    # Arrange
    response = test_client.get('/api/sharing/options')
    # Act
    option_selected = 'twitter' in response.json().get('options', [])
    # Assert
    assert option_selected, "Twitter option should be available for sharing."