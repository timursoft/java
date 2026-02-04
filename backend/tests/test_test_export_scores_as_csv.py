from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.asyncio
def test_export_scores_as_csv():
    """Test exporting user scores as CSV for a valid user."""
    # Arrange
    user_id = "valid_user_id"
    response = client.get(f"/users/{user_id}/scores/export")

    # Act
    content_disposition = response.headers.get('content-disposition')

    # Assert
    assert response.status_code == 200, "Expected status code 200 for CSV export"
    assert content_disposition is not None, "Expected 'content-disposition' header in response"
    assert "attachment; filename=" in content_disposition, "Expected attachment filename in 'content-disposition' header"