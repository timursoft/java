from fastapi.testclient import TestClient
from app.main import app

def test_double_tap_action_missing():
    """Test double-tap with missing action parameter."""
    client = TestClient(app)
    response = client.post("/tap/double-tap", json={})
    assert response.status_code == 422, "Expected status code 422 but got {response.status_code}"
    assert "detail" in response.json(), "Expected detail in response JSON"