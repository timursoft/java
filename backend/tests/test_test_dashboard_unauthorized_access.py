from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_dashboard_unauthorized_access():
    """Test if unauthorized access to dashboard is handled correctly."""
    response = client.get("/api/dashboard/trends", headers={"Authorization": "Invalid Token"})
    assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"
    assert 'detail' in response.json(), "Response JSON should contain 'detail' key for error message"