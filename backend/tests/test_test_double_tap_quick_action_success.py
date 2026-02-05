from fastapi.testclient import TestClient
from app.main import app

def test_double_tap_quick_action_success():
    """Test successful execution of quick action via double-tap."""
    client = TestClient(app)
    response = client.post("/tap/double-tap", json={"action": "boost"})
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json() == {"status": "action_executed", "action": "boost"}, "Unexpected response JSON"