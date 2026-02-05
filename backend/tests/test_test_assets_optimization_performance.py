import json
import pytest
from backend.app import create_app


def test_assets_optimization_performance():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/assets/optimize')
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    try:
        data = json.loads(response.data)
        assert 'optimization' in data, "Response JSON does not have 'optimization' key"
        assert isinstance(data['optimization'], dict), "'optimization' should be a dictionary"
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")
    except Exception as e:
        pytest.fail(f"Unexpected error in response structure: {e}")