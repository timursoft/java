import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_matchmaking_status_unavailable():
    """
    Test the matchmaking API returns a 503 error when the matchmaking service is unavailable.
    """
    # Arrange
    with patch('app.services.matchmaking.get_status', side_effect=Exception("Service Unavailable")):
        # Act
        response = client.get("/api/matchmaking/status")

        # Assert
        assert response.status_code == 503, "Expected status code 503 but got {response.status_code}"