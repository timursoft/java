import json
import pytest
from backend.app import create_app


def test_get_main_menu_invalid_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/nonexistent-endpoint')
    
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"
    
    try:
        data = json.loads(response.data)
        assert 'error' in data, "Response JSON does not have 'error' key"
        assert isinstance(data['error'], str), "'error' should be a string"
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")
    except Exception as e:
        pytest.fail(f"Unexpected error in response structure: {e}")