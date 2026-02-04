from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_apply_available_style_success():
    """
    Test that an available style can be applied successfully.
    """
    style_id = "style123"
    response = client.post(f"/api/styles/{style_id}/apply")
    assert response.status_code == 200, "Expected status code 200, got {0}".format(response.status_code)
    data = response.json()
    assert data["applied"], "Expected style to be applied, but it was not"