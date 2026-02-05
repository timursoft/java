import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_performance_metrics_stress():
    """
    Test the game's performance under simulated stress conditions to ensure it meets performance thresholds.
    """
    # Arrange
    stress_performance_metrics = {'device': 'stress'}
    
    # Act
    response = client.post("/api/game/performance-test", json=stress_performance_metrics)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['performance'] <= 150, "Expected performance to be <= 150 under stress, got {data['performance']}"