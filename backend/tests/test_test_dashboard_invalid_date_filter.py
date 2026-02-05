from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_dashboard_invalid_date_filter():
    """Test if the dashboard handles invalid date filters correctly."""
    response = client.get("/api/dashboard/feedback?start_date=invalid_date&end_date=2023-01-31")
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    assert 'detail' in response.json(), "Response JSON should contain 'detail' key for error message"