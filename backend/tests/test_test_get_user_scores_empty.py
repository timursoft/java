from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.asyncio
def test_get_user_scores_empty():
    """Test retrieval of user scores when the user has no scores."""
    # Arrange
    user_id = "user_with_no_scores"
    response = client.get(f"/users/{user_id}/scores")

    # Act
    data = response.json()

    # Assert
    assert response.status_code == 200, "Expected status code 200 for user with no scores"
    assert data == [], "Expected empty list for user with no scores"