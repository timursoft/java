def test_data_consistency_across_platforms(sync_service, mock_platform_apis):
    """Test that data is consistent across all platforms after sync."""
    # Arrange
    initial_data = {'user_id': 1, 'data': 'initial'}
    mock_platform_apis.set_data(initial_data)
    expected_data = {'user_id': 1, 'data': 'updated'}
    sync_service.update_data(expected_data)
    
    # Act
    sync_service.synchronize_data()
    
    # Assert
    for platform in mock_platform_apis.platforms:
        assert platform.get_data()['data'] == expected_data['data'], f"Data mismatch on platform {platform.name}"