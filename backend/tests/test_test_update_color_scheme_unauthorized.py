import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_update_color_scheme_unauthorized():
    """Test update color scheme endpoint without proper authorization"""
    response = client.put("/color-scheme", json={"new_scheme": {"primary": "#FFFFFF"}})
    assert response.status_code == 401, "Expected status code 401, got {response.status_code}"
    assert response.json()["detail"] == "Not authenticated", "Unexpected error message when unauthorized"
