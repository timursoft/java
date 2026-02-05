import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_game_adapt_screen_size_desktop():
    """
    Test that the game adapts correctly to a standard desktop screen size without layout issues.
    """
    # Arrange
    desktop_screen_size = {'width': 1920, 'height': 1080}
    
    # Act
    response = client.post("/api/game/responsive-test", json=desktop_screen_size)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['layout'] == 'ok', "Expected layout to be 'ok', got {data['layout']}"