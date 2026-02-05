import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_get_layout_invalid_token():
    """Test retrieval of the layout with an invalid token"""
    # Arrange
    headers = {"Authorization": "Bearer invalid_token"}
    
    # Act
    response = client.get("/api/layout", headers=headers)

    # Assert
    assert response.status_code == 401, "Expected status code 401, but got {response.status_code}"