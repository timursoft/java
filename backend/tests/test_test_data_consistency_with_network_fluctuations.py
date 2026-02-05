def test_data_consistency_with_network_fluctuations(sync_service, mock_platform_apis, simulate_network_fluctuations):
    """Test that data remains consistent across platforms even with network fluctuations."""
    # Arrange
    initial_data = {'user_id': 2, 'data': 'initial'}
    mock_platform_apis.set_data(initial_data)
    sync_service.update_data({'user_id': 2, 'data': 'updated'})
    
    # Act
    with simulate_network_fluctuations():
        sync_service.synchronize_data()
    
    # Assert
    for platform in mock_platform_apis.platforms:
        assert platform.get_data()['data'] == 'updated', f"Data mismatch due to network fluctuation on platform {platform.name}"