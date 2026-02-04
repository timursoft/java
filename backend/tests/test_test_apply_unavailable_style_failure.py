from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_apply_unavailable_style_failure():
    """
    Test that trying to apply an unavailable style fails as expected.
    """
    style_id = "unavailable_style"
    response = client.post(f"/api/styles/{style_id}/apply")
    assert response.status_code == 400, "Expected status code 400, got {0}".format(response.status_code)
    data = response.json()
    assert "error" in data, "Response JSON missing 'error' key"
    assert data["error"] == "Style is unavailable", "Unexpected error message: {0}".format(data["error"])