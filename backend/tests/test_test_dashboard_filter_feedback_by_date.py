from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_dashboard_filter_feedback_by_date():
    """Test if feedback can be filtered by date."""
    response = client.get("/api/dashboard/feedback?start_date=2023-01-01&end_date=2023-01-31")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert 'feedback' in response.json(), "Response JSON should contain 'feedback' key"
    # Further assertions for date range can be added here