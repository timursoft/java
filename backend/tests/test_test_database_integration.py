from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_database_integration():
    """Test integration with the database to ensure data consistency."""
    response = client.get('/api/data')
    assert response.status_code == 200, "API did not return a successful response"
    assert response.json() == {'key': 'value'}, "API response data is incorrect"