import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_update_layout_forbidden():
    """Test update layout with insufficient permissions"""
    # Arrange
    headers = {"Authorization": "Bearer user_token"}
    payload = {"layout": "modern"}
    
    # Act
    response = client.put("/api/layout", headers=headers, json=payload)

    # Assert
    assert response.status_code == 403, "Expected status code 403, but got {response.status_code}"