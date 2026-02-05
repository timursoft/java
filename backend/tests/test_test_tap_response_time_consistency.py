from fastapi.testclient import TestClient
from app.main import app
import time

@pytest.mark.parametrize("endpoint", ["/tap/select", "/tap/double-tap"])
def test_tap_response_time_consistency(endpoint):
    """Test the consistency of response time for tap actions."""
    client = TestClient(app)
    start_time = time.time()
    response = client.post(endpoint, json={"option": "test"})
    response_time = time.time() - start_time
    assert response_time < 0.5, f"Response time {response_time} exceeded 0.5 seconds"