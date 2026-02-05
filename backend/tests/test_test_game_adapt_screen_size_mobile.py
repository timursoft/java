import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_game_adapt_screen_size_mobile():
    """
    Test that the game adapts correctly to a standard mobile screen size without layout issues.
    """
    # Arrange
    mobile_screen_size = {'width': 375, 'height': 667}
    
    # Act
    response = client.post("/api/game/responsive-test", json=mobile_screen_size)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['layout'] == 'ok', "Expected layout to be 'ok', got {data['layout']}"