def test_linked_accounts_edge_case_large_progress_data(api_client, mocker):
    """
    Test that account linking works with large progress data.
    """
    # Arrange
    large_progress = {'level': 1000, 'score': 1000000}
    mocker.patch('external_service.get_shared_progress', return_value=large_progress)
    email = 'test@example.com'
    data = {'email': email}

    # Act
    response = api_client.post('/link-account', json=data)

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()['progress'] == large_progress, "Expected successful linking with large progress data"