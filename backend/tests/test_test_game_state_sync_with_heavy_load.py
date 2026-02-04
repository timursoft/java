import pytest
from unittest.mock import MagicMock

@pytest.mark.asyncio
def test_game_state_sync_with_heavy_load(sync_function):
    """Test game state synchronization under heavy network load."""
    # Arrange
    sync_function = MagicMock()
    heavy_load = True  # Simulate heavy network load
    
    # Act
    sync_function(heavy_load)

    # Assert
    sync_function.assert_called_with(heavy_load)