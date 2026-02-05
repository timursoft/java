import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_color_palette_approval_status():
    """Verify the color palette approval by stakeholders"""
    response = client.get("/color-scheme/approval-status")
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert response.json()["approved"] is True, "Color palette has not been approved by stakeholders"
