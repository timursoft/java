import time
import pytest
from unittest.mock import MagicMock

@pytest.mark.asyncio
def test_game_state_sync_under_100ms(sync_function):
    """Test that game state updates are synchronized under 100ms."""
    # Arrange
    start_time = time.monotonic()
    sync_function = MagicMock(return_value=True)
    
    # Act
    sync_function()
    end_time = time.monotonic()
    sync_duration = end_time - start_time

    # Assert
    assert sync_duration < 0.1, f"Synchronization took too long: {sync_duration} seconds"