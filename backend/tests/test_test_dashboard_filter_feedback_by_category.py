from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_dashboard_filter_feedback_by_category():
    """Test if feedback can be filtered by category."""
    response = client.get("/api/dashboard/feedback?category=bug")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert 'feedback' in response.json(), "Response JSON should contain 'feedback' key"
    # Further assertions for category matching can be added here