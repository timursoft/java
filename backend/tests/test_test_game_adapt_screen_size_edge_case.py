import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
def test_game_adapt_screen_size_edge_case():
    """
    Test edge case screen size to ensure the game handles unusual dimensions gracefully.
    """
    # Arrange
    edge_case_screen_size = {'width': 1000, 'height': 1000}
    
    # Act
    response = client.post("/api/game/responsive-test", json=edge_case_screen_size)
    
    # Assert
    assert response.status_code == 200, "Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data['layout'] == 'ok', "Expected layout to be 'ok', got {data['layout']}"