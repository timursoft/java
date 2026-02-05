def test_sync_failure_handling(sync_service, mock_platform_apis):
    """Test system's ability to handle synchronization failures gracefully."""
    # Arrange
    sync_service.simulate_failure = True
    
    # Act & Assert
    with pytest.raises(Exception, match='Synchronization failed'):  
        sync_service.synchronize_data()