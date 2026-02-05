def test_bug_related_edge_case(client):
    """
    Test an edge case that was previously causing the bug.
    """
    # Arrange
    response = client.get("/api/buggy-endpoint?param=unexpected_value")
    # Act
    # Assert
    assert response.status_code == 200, "Expected status code 200 for edge case, but got {response.status_code}"
    assert "error" not in response.json(), "Edge case should not produce an error."