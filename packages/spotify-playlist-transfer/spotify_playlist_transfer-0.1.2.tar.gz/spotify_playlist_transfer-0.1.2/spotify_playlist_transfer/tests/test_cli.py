from typer.testing import CliRunner
from spotify_playlist_transfer.cli import app

runner = CliRunner()

def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Transfer Spotify content" in result.output

def test_setup_flow(mocker):
    mock_setup = mocker.patch("spotify_playlist_transfer.cli.manager.setup_credentials")
    result = runner.invoke(app, ["setup"])
    assert mock_setup.called
    assert result.exit_code == 0