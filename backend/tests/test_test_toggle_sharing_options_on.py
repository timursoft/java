from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_toggle_sharing_options_on():
    """Test that user can toggle sharing options on."""
    # Arrange
    data = {"share_option": True}
    headers = {"Authorization": "Bearer valid_token"}

    # Act
    response = client.post("/api/settings/share", json=data, headers=headers)

    # Assert
    assert response.status_code == 200, "Expected status code 200 for successful toggle"
    assert response.json()["success"] is True, "Expected success to be True when toggling on"