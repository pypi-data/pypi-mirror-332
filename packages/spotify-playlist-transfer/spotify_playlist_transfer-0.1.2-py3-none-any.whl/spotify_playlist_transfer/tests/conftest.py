import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_spotify():
    mock = Mock()
    mock.me.return_value = {"id": "test_user", "display_name": "Test User"}
    return mock