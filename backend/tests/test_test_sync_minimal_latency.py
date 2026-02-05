def test_sync_minimal_latency(sync_service, mock_platform_apis):
    """Test that synchronization completes with minimal latency."""
    # Arrange
    sync_service.set_latency_threshold(100)  # 100ms as an acceptable threshold
    
    # Act
    start_time = time.time()
    sync_service.synchronize_data()
    end_time = time.time()
    
    # Assert
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    assert elapsed_time <= sync_service.latency_threshold, f"Sync latency {elapsed_time}ms exceeded threshold"