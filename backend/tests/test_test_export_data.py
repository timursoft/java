from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_export_data():
    """Test if the export option works correctly."""
    response = client.get("/api/dashboard/export")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert 'export_data' in response.json(), "Response JSON should contain 'export_data' key"