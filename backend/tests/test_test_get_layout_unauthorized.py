import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_get_layout_unauthorized():
    """Test retrieval of the layout without authentication"""
    # Arrange
    headers = {}
    
    # Act
    response = client.get("/api/layout", headers=headers)

    # Assert
    assert response.status_code == 401, "Expected status code 401, but got {response.status_code}"