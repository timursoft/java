from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_main_menu_success():
    """Test main menu endpoint returns correct options."""
    response = client.get("/api/menu")
    assert response.status_code == 200, "Expected status code 200"
    expected_options = {"options": ["Play", "Settings", "Exit"]}
    assert response.json() == expected_options, f"Expected menu options: {expected_options}"