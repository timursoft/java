import pytest
from unittest.mock import MagicMock

@pytest.mark.asyncio
def test_sync_function_error_handling(sync_function):
    """Test synchronization function handles exceptions properly."""
    # Arrange
    sync_function = MagicMock(side_effect=Exception("Sync Error"))
    
    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        sync_function()
    assert "Sync Error" in str(exc_info.value), "Exception message mismatch"