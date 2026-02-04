from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_preview_style_success():
    """
    Test that a style can be previewed successfully before application.
    """
    style_id = "style123"
    response = client.get(f"/api/styles/{style_id}/preview")
    assert response.status_code == 200, "Expected status code 200, got {0}".format(response.status_code)
    data = response.json()
    assert "preview_url" in data, "Response JSON missing 'preview_url' key"
    assert isinstance(data["preview_url"], str), "'preview_url' should be a string"