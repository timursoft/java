import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_get_layout_success():
    """Test successful retrieval of the layout with valid authentication"""
    # Arrange
    headers = {"Authorization": "Bearer valid_token"}
    
    # Act
    response = client.get("/api/layout", headers=headers)

    # Assert
    assert response.status_code == 200, "Expected status code 200, but got {response.status_code}"
    assert "layout" in response.json(), "Response JSON does not contain 'layout' key"
    assert response.json()["layout"] == "modern", "Layout is not as expected"