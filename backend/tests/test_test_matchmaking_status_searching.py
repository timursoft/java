import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_matchmaking_status_searching():
    """
    Test the matchmaking API returns 'searching' status when matchmaking is ongoing.
    """
    # Arrange
    # Mock the matchmaking status to be 'searching'
    response = client.get("/api/matchmaking/status")

    # Act
    # Assert
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json().get("status") == "searching", "Expected status 'searching' but got {response.json().get('status')}"