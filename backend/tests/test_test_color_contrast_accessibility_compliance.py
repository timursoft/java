import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_color_contrast_accessibility_compliance():
    """Test if the color contrast meets accessibility standards"""
    response = client.get("/color-scheme/accessibility-check")
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    assert response.json()["accessibility_compliant"] is True, "Color contrast does not meet accessibility standards"
