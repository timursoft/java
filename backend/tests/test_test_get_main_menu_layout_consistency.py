import json
import pytest
from backend.app import create_app


def test_get_main_menu_layout_consistency():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/main-menu-layout')
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    try:
        data = json.loads(response.data)
        assert 'layout' in data, "Response JSON does not have 'layout' key"
        assert isinstance(data['layout'], dict), "'layout' should be a dictionary"
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")
    except Exception as e:
        pytest.fail(f"Unexpected error in response structure: {e}")