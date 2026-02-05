import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_post_layout_success():
    """Test successful posting of a new layout by an admin user"""
    # Arrange
    headers = {"Authorization": "Bearer admin_token"}
    payload = {"layout": "modern"}
    
    # Act
    response = client.post("/api/layout", headers=headers, json=payload)

    # Assert
    assert response.status_code == 201, "Expected status code 201, but got {response.status_code}"
    assert response.json()["layout"] == "modern", "Layout is not as expected after posting"