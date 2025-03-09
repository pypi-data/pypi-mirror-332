import pytest
from unittest.mock import patch, MagicMock
from spotify_playlist_transfer.utils import SpotifyManager
from spotipy import SpotifyOauthError
from spotify_playlist_transfer.cli import handle_authentication
import spotipy

def test_load_credentials_success():
    with patch("keyring.get_password") as mock_get:
        mock_get.side_effect = lambda service, key: f"mock_{key}"
        manager = SpotifyManager()
        assert manager.load_credentials() is True
        assert manager.credentials["client_id"] == "mock_client_id"

def test_port_conflict_handling(mocker):
    manager = SpotifyManager()
    
    # Mock port check sequence
    mock_bind = mocker.patch("socket.socket.bind")
    mock_bind.side_effect = [
        OSError(48, 'Address already in use'),  # First call fails
        None  # Second call succeeds
    ]
    
    # Mock port conflict handler
    mock_handler = mocker.patch.object(manager, "handle_port_conflict")
    
    # Mock Spotify client creation
    mock_client = mocker.MagicMock()
    mocker.patch.object(manager, "_create_spotify_client", return_value=mock_client)
    
    result = manager.authenticate("test")
    
    # Verify behavior
    mock_handler.assert_called_once()
    assert mock_bind.call_count == 2
    assert result == mock_client

