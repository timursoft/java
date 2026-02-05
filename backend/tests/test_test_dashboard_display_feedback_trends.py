from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_dashboard_display_feedback_trends():
    """Test if the dashboard endpoint returns feedback trends successfully."""
    response = client.get("/api/dashboard/trends")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert 'trends' in response.json(), "Response JSON should contain 'trends' key"