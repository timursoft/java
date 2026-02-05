import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_get_color_scheme_not_found():
    """Test retrieval of a non-existent color scheme"""
    response = client.get("/color-scheme/non-existent")
    assert response.status_code == 404, "Expected status code 404, got {response.status_code}"
    assert response.json()["detail"] == "Color scheme not found", "Unexpected error message"
