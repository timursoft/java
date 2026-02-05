import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_performance_metrics_mobile():
    """
    Test that the game's performance metrics are within acceptable thresholds on a mobile device.
    """
    # Arrange
    mobile_performance_metrics = {'device': 'mobile'}
    
    # Act
    response = client.post("/api/game/performance-test", json=mobile_performance_metrics)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['performance'] <= 100, "Expected performance to be <= 100, got {data['performance']}"