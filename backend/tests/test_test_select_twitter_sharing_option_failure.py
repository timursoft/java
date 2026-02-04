def test_select_twitter_sharing_option_failure(test_client, mocker):
    """Test failure scenario where Twitter sharing option is unavailable."""
    # Arrange
    mocker.patch('api.sharing.get_options', return_value={'options': ['email', 'facebook']})
    response = test_client.get('/api/sharing/options')
    # Act
    option_selected = 'twitter' in response.json().get('options', [])
    # Assert
    assert not option_selected, "Twitter option should not be available when it is disabled."