from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.asyncio
def test_get_user_scores_success():
    """Test successful retrieval of user scores for a valid user."""
    # Arrange
    user_id = "valid_user_id"
    response = client.get(f"/users/{user_id}/scores")

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert data is not None, "Expected non-null data"
    assert isinstance(data, list), "Expected data to be a list"
    assert all(isinstance(score, dict) for score in data), "Expected all scores to be dictionaries"