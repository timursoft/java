import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_performance_metrics_desktop():
    """
    Test that the game's performance metrics are within acceptable thresholds on a desktop device.
    """
    # Arrange
    desktop_performance_metrics = {'device': 'desktop'}
    
    # Act
    response = client.post("/api/game/performance-test", json=desktop_performance_metrics)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['performance'] <= 100, "Expected performance to be <= 100, got {data['performance']}"