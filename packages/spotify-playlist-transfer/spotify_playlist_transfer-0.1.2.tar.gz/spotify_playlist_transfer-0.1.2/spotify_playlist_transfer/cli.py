import time
from pathlib import Path
from typing import Optional, Dict, Set
from loguru import logger
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
import typer
from spotify_playlist_transfer.utils import SpotifyManager
from spotipy import SpotifyException

app = typer.Typer(rich_markup_mode="markdown")
console = Console()
manager = SpotifyManager()

@app.command()
def setup():
    """Initial setup for Spotify API credentials"""
    if manager.setup_credentials():
        console.print("\n[bold green]✅ Setup completed successfully![/]")
    else:
        console.print("\n[red]❌ Setup failed. See errors above.[/]")
        raise typer.Exit(1)

@app.command()
def transfer(
    reuse: bool = typer.Option(False, "--reuse", help="Reuse previous authentication"),
    change_account: Optional[str] = typer.Option(None, help="Re-authenticate specific account (source/destination)"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed debug info")
):
    """Transfer Spotify content between accounts"""
    manager.set_log_level(verbose)
    
    if not manager.load_credentials():
        console.print("\n[red]❌ No credentials found! Run 'setup' first[/]")
        raise typer.Exit(1)

    try:
        source_sp, dest_sp = handle_authentication(reuse, change_account)
        transfer_content(source_sp, dest_sp)
        console.print("\n[bold green]✅ Transfer completed successfully![/]")
    except Exception as e:
        if not isinstance(e, typer.Exit):
            console.print(f"\n[red]❌ Fatal error: {str(e)}[/]")
        raise typer.Exit(1) from e

def handle_authentication(reuse: bool, change_account: Optional[str]):
    """Authentication flow with retries"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return _authenticate_accounts(reuse, change_account)
        except typer.Exit as e:
            if e.exit_code == 0:
                raise e
            if attempt == max_retries - 1:
                console.print("\n[red]❌ Maximum authentication attempts reached[/]")
                raise e
            console.print(f"\n[yellow]↻ Retrying ({attempt + 1}/3)...[/]")
            time.sleep(1)

def _authenticate_accounts(reuse: bool, change_account: Optional[str]):
    """Perform actual authentication"""
    cache_files = {
        "source": Path(".spotify_source_cache"),
        "destination": Path(".spotify_destination_cache")
    }

    if change_account and change_account.lower() in cache_files:
        cache_files[change_account.lower()].unlink(missing_ok=True)
        console.print(f"\n[bold yellow]🔑 Re-authenticating {change_account} account[/]")

    console.print("\n[bold yellow]🔑 Source Account Authentication[/]")
    source_sp = authenticate_account("source", reuse, cache_files["source"])
    
    console.print("\n[bold yellow]🔑 Destination Account Authentication[/]")
    dest_sp = authenticate_account("destination", reuse, cache_files["destination"])

    verify_different_accounts(source_sp, dest_sp)
    return source_sp, dest_sp

def authenticate_account(account_type: str, reuse: bool, cache_path: Path):
    """Authenticate individual account"""
    if reuse and cache_path.exists():
        try:
            sp = manager.authenticate(account_type)
            user = manager.get_user_info(sp)
            console.print(f"[green]✓ Using cached {account_type}: {user['name']}[/]")
            return sp
        except Exception as e:
            logger.debug(f"Cache reuse failed: {str(e)}")
    
    console.print(f"[yellow]Awaiting {account_type} authentication in browser...[/]")
    sp = manager.authenticate(account_type, force_reauthenticate=True)
    user = manager.get_user_info(sp)
    console.print(f"[green]✓ Authenticated as {user['name']}[/]")
    return sp

def verify_different_accounts(source_sp, dest_sp):
    """Ensure source and destination are different"""
    source_id = manager.get_user_info(source_sp)["id"]
    dest_id = manager.get_user_info(dest_sp)["id"]
    
    if source_id == dest_id:
        console.print("\n[red]❌ Error: Source and destination accounts are the same![/]")
        raise typer.Exit(1)

def transfer_content(source_sp, dest_sp):
    """Handle content transfer workflow"""
    transfer_playlists = Confirm.ask("\n[bold]Transfer playlists?[/]", default=True)
    content = manager.get_transfer_content(source_sp, transfer_playlists)

    with Progress(SpinnerColumn(), TextColumn("{task.description}"), transient=True) as progress:
        # Transfer liked songs
        progress.add_task("Processing liked songs...")
        transfer_liked(content["liked_songs"], dest_sp)

        # Transfer playlists
        if transfer_playlists:
            selected = select_playlists(content["playlists"])
            for pl_id in selected:
                progress.add_task(f"Transferring {content['playlists'][pl_id]['name']}...")
                transfer_playlist(content["playlists"][pl_id], dest_sp)

def select_playlists(playlists: Dict) -> list:
    """Interactive playlist selection"""
    table = Table(title="Your Playlists", show_header=True)
    table.add_column("#", style="dim")
    table.add_column("Name")
    table.add_column("Tracks", justify="right")
    
    for idx, (pl_id, details) in enumerate(playlists.items(), 1):
        table.add_row(str(idx), details['name'], str(len(details['tracks'])))
    
    console.print(table)
    choices = Prompt.ask("Select playlists (comma-separated)", choices=[str(i) for i in range(1, len(playlists)+1)])
    
    return [list(playlists.keys())[int(i)-1] for i in choices.split(",")]

def transfer_liked(track_ids: Set[str], dest_sp):
    """Transfer liked songs"""
    existing = set(manager._paginated_get(
        dest_sp.current_user_saved_tracks,
        lambda r: [item["track"]["id"] for item in r["items"] if item["track"]]
    ))
    new_tracks = track_ids - existing
    
    if new_tracks:
        dest_sp.current_user_saved_tracks_add(list(new_tracks))
        console.print(f"\n[green]Added {len(new_tracks)} liked songs[/]")
    else:
        console.print("\n[yellow]No new liked songs to transfer[/]")

def transfer_playlist(pl_data: Dict, dest_sp):
    """Transfer individual playlist"""
    try:
        # Check existing playlists
        dest_playlists = manager._paginated_get(
            dest_sp.current_user_playlists,
            lambda r: [(pl["id"], pl["name"]) for pl in r["items"]]
        )
        
        # Handle conflicts
        existing = next((pid for pid, name in dest_playlists if name == pl_data["name"]), None)
        if existing:
            action = Prompt.ask(
                f"[yellow]'{pl_data['name']}' exists![/]",
                choices=["skip", "append", "replace"],
                default="skip"
            )
            if action == "skip": return
            if action == "replace": dest_sp.current_user_unfollow_playlist(existing)
        
        # Create/update playlist
        pl = dest_sp.user_playlist_create(
            user=manager.get_user_info(dest_sp)["id"],
            name=pl_data["name"],
            public=False
        )
        
        # Add tracks
        for i in range(0, len(pl_data["tracks"]), 100):
            batch = pl_data["tracks"][i:i+100]
            dest_sp.playlist_add_items(pl["id"], batch)
        
        console.print(f"[green]Transferred {pl_data['name']} ({len(pl_data['tracks'])} tracks)[/]")
        
    except SpotifyException as e:
        console.print(f"\n[red]Error transferring {pl_data['name']}: {e.msg}[/]")

if __name__ == "__main__":
    app()