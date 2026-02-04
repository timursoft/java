import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_matchmaking_status_no_auth():
    """
    Test the matchmaking API returns a 401 error when no authentication is provided.
    """
    # Arrange
    headers = {}

    # Act
    response = client.get("/api/matchmaking/status", headers=headers)

    # Assert
    assert response.status_code == 401, "Expected status code 401 but got {response.status_code}"