from fastapi.testclient import TestClient
from app.main import app

def test_tap_select_option_success():
    """Test successful selection of game option via tap."""
    client = TestClient(app)
    response = client.post("/tap/select", json={"option": "start_game"})
    assert response.status_code == 200, "Expected status code 200 but got {response.status_code}"
    assert response.json() == {"status": "selected", "option": "start_game"}, "Unexpected response JSON"