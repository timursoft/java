from fastapi.testclient import TestClient
from app.main import app

def test_tap_select_option_empty():
    """Test handling of empty game option tap."""
    client = TestClient(app)
    response = client.post("/tap/select", json={"option": ""})
    assert response.status_code == 400, "Expected status code 400 but got {response.status_code}"
    assert "error" in response.json(), "Expected error in response JSON"