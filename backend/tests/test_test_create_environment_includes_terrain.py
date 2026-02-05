import json
import pytest
from backend.app import create_app


def test_create_environment_includes_terrain():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/environment')
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    try:
        data = json.loads(response.data)
        assert 'terrain' in data, "Response JSON does not have 'terrain' key"
        assert isinstance(data['terrain'], dict), "'terrain' should be a dictionary"
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")
    except Exception as e:
        pytest.fail(f"Unexpected error in response structure: {e}")