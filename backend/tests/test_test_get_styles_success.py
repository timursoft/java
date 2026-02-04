from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_get_styles_success():
    """
    Test that the styles are successfully retrieved with correct categories and items.
    """
    response = client.get("/api/styles")
    assert response.status_code == 200, "Expected status code 200, got {0}".format(response.status_code)
    data = response.json()
    assert "categories" in data, "Response JSON missing 'categories' key"
    assert isinstance(data["categories"], list), "'categories' should be a list"
    assert len(data["categories"]) > 0, "'categories' list is empty"
    assert "styles" in data, "Response JSON missing 'styles' key"
    assert isinstance(data["styles"], list), "'styles' should be a list"
    assert len(data["styles"]) > 0, "'styles' list is empty"