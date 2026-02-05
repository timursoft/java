from unittest.mock import patch

def test_mock_external_dependencies():
    """Ensure external dependencies are properly mocked during regression tests."""
    with patch('external_service.call') as mock_call:
        mock_call.return_value = 'mocked_response'
        response = external_service.call()
        assert response == 'mocked_response', "External service call was not mocked correctly"