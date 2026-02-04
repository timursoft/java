import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_matchmaking_status_invalid():
    """
    Test the matchmaking API returns a 400 error when an invalid request is made.
    """
    # Arrange
    invalid_status = "invalid"

    # Act
    response = client.get(f"/api/matchmaking/status/{invalid_status}")

    # Assert
    assert response.status_code == 400, "Expected status code 400 but got {response.status_code}"