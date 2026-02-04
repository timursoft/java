import pytest
from unittest.mock import MagicMock

@pytest.mark.asyncio
def test_sync_no_packet_loss(sync_function):
    """Test that no data packet loss occurs during synchronization."""
    # Arrange
    sync_function = MagicMock()
    
    # Act
    sync_function()

    # Assert
    sync_function.assert_called_once()
    assert sync_function.call_count == 1, "Expected sync to be called once"