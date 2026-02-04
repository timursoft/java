import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_matchmaking_status_matched():
    """
    Test the matchmaking API returns 'matched' status when an opponent is found.
    """
    # Arrange
    # Mock the matchmaking status to be 'matched'
    response = client.get("/api/matchmaking/status")

    # Act
    # Assert
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json().get("status") == "matched", "Expected status 'matched' but got {response.json().get('status')}"