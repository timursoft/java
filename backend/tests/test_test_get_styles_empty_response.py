from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_get_styles_empty_response(mocker):
    """
    Test the response when no styles are available to ensure graceful handling.
    """
    mocker.patch("myapp.db.get_styles", return_value={"categories": [], "styles": []})
    response = client.get("/api/styles")
    assert response.status_code == 200, "Expected status code 200, got {0}".format(response.status_code)
    data = response.json()
    assert data["categories"] == [], "Expected empty 'categories' list, got {0}".format(data["categories"]) 
    assert data["styles"] == [], "Expected empty 'styles' list, got {0}".format(data["styles"])