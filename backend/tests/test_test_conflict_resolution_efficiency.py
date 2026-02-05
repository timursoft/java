def test_conflict_resolution_efficiency(sync_service, mock_platform_apis):
    """Test conflict resolution efficiency during synchronization."""
    # Arrange
    conflicting_data = {'user_id': 1, 'data': 'conflict'}
    mock_platform_apis.set_conflicting_data(conflicting_data)
    resolution_strategy = 'latest'
    sync_service.set_conflict_resolution_strategy(resolution_strategy)
    
    # Act
    sync_service.synchronize_data()
    
    # Assert
    for platform in mock_platform_apis.platforms:
        assert platform.get_data()['data'] == conflicting_data['data'], f"Conflict not resolved correctly on platform {platform.name}"