@pytest.mark.performance
def test_high_performance_read_write(leaderboard_service):
    """Test high performance of leaderboard read and write operations."""
    # Arrange
    data = [{'user_id': f'user{i}', 'score': i * 10} for i in range(1000)]

    # Act
    for item in data:
        leaderboard_service.store_data(item)

    # Assert
    start_time = time.time()
    result = leaderboard_service.retrieve_data('user500')
    end_time = time.time()
    assert (end_time - start_time) < 0.5, "Read operation should be performed under 500ms"
    assert result is not None, "Data should be retrieved successfully"