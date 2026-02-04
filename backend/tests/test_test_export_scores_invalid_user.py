from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.asyncio
def test_export_scores_invalid_user():
    """Test exporting user scores as CSV with an invalid user ID."""
    # Arrange
    user_id = "invalid_user_id"
    response = client.get(f"/users/{user_id}/scores/export")

    # Act
    
    # Assert
    assert response.status_code == 404, "Expected status code 404 for invalid user during CSV export"