import os
import sys
import time
import json
import socket
import webbrowser
from pathlib import Path
from urllib.parse import urlparse
from typing import Dict, List, Set, Optional
import keyring
from loguru import logger
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
from spotipy.exceptions import SpotifyException
import typer

class SpotifyManager:
    def __init__(self):
        self.service_name = "spotify-transfer-tool"
        self.credentials = {
            "client_id": None,
            "client_secret": None,
            "redirect_uri": None
        }
        self.current_port = 8888
        self.set_log_level(False)

    def set_log_level(self, verbose: bool):
        """Configure logging verbosity"""
        logger.remove()
        if verbose:
            logger.add(sys.stderr, level="DEBUG")
        else:
            logger.add(sys.stderr, level="INFO")

    def setup_credentials(self) -> bool:
        """Interactively setup and store credentials"""
        from rich.prompt import Prompt
        from rich.console import Console
        console = Console()

        try:
            console.print("\n[bold yellow]🔐 Spotify API Setup Guide[/]", justify="center")
            console.print("1. Go to [bold]https://developer.spotify.com/dashboard[/]")
            console.print("2. Create app and set Redirect URI to [green]http://localhost:8888/callback[/]")
            console.print("3. Copy Client ID and Client Secret\n")
            
            client_id = Prompt.ask("[bold]Enter Client ID[/]")
            client_secret = Prompt.ask("[bold]Enter Client Secret[/]", password=True)
            redirect_uri = Prompt.ask(
                "[bold]Enter Redirect URI[/] (press Enter for default)",
                default="http://localhost:8888/callback"
            )

            if not self._validate_credentials(client_id, client_secret):
                raise ValueError("Invalid credentials format")

            keyring.set_password(self.service_name, "client_id", client_id)
            keyring.set_password(self.service_name, "client_secret", client_secret)
            keyring.set_password(self.service_name, "redirect_uri", redirect_uri)
            
            console.print("\n[green]✅ Credentials stored securely![/]")
            return True
            
        except Exception as e:
            logger.error(f"Setup failed: {str(e)}")
            console.print("\n[red]❌ Setup error:[/] " + str(e))
            return False

    def _validate_credentials(self, client_id: str, client_secret: str) -> bool:
        """Validate credential format"""
        return len(client_id) == 32 and len(client_secret) == 32

    def load_credentials(self) -> bool:
        """Load credentials from system keyring"""
        try:
            self.credentials["client_id"] = keyring.get_password(self.service_name, "client_id")
            self.credentials["client_secret"] = keyring.get_password(self.service_name, "client_secret")
            self.credentials["redirect_uri"] = keyring.get_password(self.service_name, "redirect_uri")
            
            if not all(self.credentials.values()):
                raise ValueError("Missing credentials in keyring")
            
            parsed = urlparse(self.credentials["redirect_uri"])
            self.current_port = parsed.port or 8888
            return True
        except Exception as e:
            logger.error(f"Credential load failed: {str(e)}")
            return False

    def authenticate(self, account_type: str, force_reauthenticate: bool = False) -> Optional[spotipy.Spotify]:
        """Handle authentication with port conflict resolution"""
        cache_path = Path(f".spotify_{account_type}_cache")
        
        if force_reauthenticate and cache_path.exists():
            cache_path.unlink()

        try:
            # Check port availability
            self._check_port_available()
            return self._create_spotify_client(cache_path)
            
        except OSError as e:
            if e.errno == 48:  # Address already in use
                self.handle_port_conflict()
                return self.authenticate(account_type, True)
            raise
        except SpotifyOauthError as e:
            logger.error(f"Authentication failed: {str(e)}")
            if cache_path.exists():
                cache_path.unlink()
            return None

    def _create_spotify_client(self, cache_path: Path) -> spotipy.Spotify:
        """Create Spotify client with current config"""
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.credentials["client_id"],
            client_secret=self.credentials["client_secret"],
            redirect_uri=self.credentials["redirect_uri"],
            scope=" ".join([
                "user-library-read",
                "user-library-modify",
                "playlist-read-private",
                "playlist-modify-private",
                "playlist-modify-public"
            ]),
            cache_path=str(cache_path)
        ))

    def _check_port_available(self):
        """Verify port is available"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', self.current_port))

    def handle_port_conflict(self):
        """Interactive port conflict resolution"""
        from rich.console import Console
        from rich.prompt import Confirm, Prompt
        console = Console()
        
        console.print("\n[bold red]⚠️ Port Conflict Detected[/]")
        console.print(f"Port {self.current_port} is already in use.")
        console.print("[yellow]Choose resolution:[/]")
        console.print("1. Find new port automatically")
        console.print("2. Manually specify different port")
        console.print("3. Exit and resolve manually\n")

        choice = Prompt.ask("Select option (1-3)", choices=["1", "2", "3"], default="1")
        
        if choice == "1":
            new_port = self._find_available_port()
            self._update_port_config(new_port)
        elif choice == "2":
            while True:
                port_input = Prompt.ask("Enter port number (1024-65535)")
                try:
                    new_port = int(port_input)
                    if 1024 <= new_port <= 65535:
                        break
                    console.print("[red]Port must be between 1024 and 65535![/]")
                except ValueError:
                    console.print("[red]Invalid port number! Please enter a number.[/]")
            self._update_port_config(new_port)
        else:
            console.print("\n[yellow]Please close conflicting applications and try again[/]")
            raise typer.Exit(0)

    def _find_available_port(self, start_port=8888) -> int:
        """Find next available port"""
        for port in range(start_port, start_port + 50):
            with socket.socket() as s:
                try:
                    s.bind(('localhost', port))
                    return port
                except OSError:
                    continue
        raise OSError("No available ports found")

    def _update_port_config(self, new_port: int):
        """Update configuration with new port"""
        from rich.console import Console
        from rich.prompt import Confirm
        console = Console()
        
        new_uri = f"http://localhost:{new_port}/callback"
        keyring.set_password(self.service_name, "redirect_uri", new_uri)
        self.credentials["redirect_uri"] = new_uri
        self.current_port = new_port
        
        console.print(f"\n[green]✓ Using port {new_port}[/]")
        console.print("[yellow]Important:[/] Update Spotify Dashboard with:")
        console.print(f"[bold]{new_uri}[/]")
        
        if Confirm.ask("\nOpen Spotify Dashboard in browser?"):
            webbrowser.open("https://developer.spotify.com/dashboard")
        
        console.print("\n[bold]Press Enter after updating Dashboard...[/]")
        input()

    def get_user_info(self, sp: spotipy.Spotify) -> Dict:
        """Get authenticated user info"""
        user = sp.me()
        return {
            "id": user["id"],
            "name": user.get("display_name", "Unknown"),
            "email": user.get("email", "Unknown")
        }

    def get_transfer_content(self, sp: spotipy.Spotify, transfer_playlists: bool) -> Dict:
        """Get content for transfer"""
        content = {"liked_songs": set(), "playlists": {}}
        
        # Get liked songs
        content["liked_songs"] = self._paginated_get(
            sp.current_user_saved_tracks,
            lambda r: [item["track"]["id"] for item in r["items"] if item["track"]]
        )

        # Get playlists if requested
        if transfer_playlists:
            playlists = self._paginated_get(
                sp.current_user_playlists,
                lambda r: [
                    (pl["id"], pl["name"]) 
                    for pl in r["items"] 
                    if pl["owner"]["id"] == self.get_user_info(sp)["id"]
                ]
            )
            
            for pl_id, pl_name in playlists:
                content["playlists"][pl_id] = {
                    "name": pl_name,
                    "tracks": self._paginated_get(
                        lambda limit, offset: sp.playlist_items(pl_id, limit=limit, offset=offset),
                        lambda r: [item["track"]["id"] for item in r["items"] if item["track"]]
                    )
                }
        
        return content

    def _paginated_get(self, api_method, data_extractor):
        """Handle paginated API calls"""
        results = []
        offset = 0
        while True:
            response = api_method(limit=50, offset=offset)
            results.extend(data_extractor(response))
            
            if len(response["items"]) < 50:
                break
            offset += 50
            time.sleep(0.2)
        return results