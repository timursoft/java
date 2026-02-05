import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_get_color_scheme_success():
    """Test successful retrieval of the current color scheme"""
    response = client.get("/color-scheme")
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert "color_scheme" in response.json(), "Response JSON does not contain 'color_scheme'"
