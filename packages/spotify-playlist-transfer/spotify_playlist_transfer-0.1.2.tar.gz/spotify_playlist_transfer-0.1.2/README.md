# Spotify Transfer Tool 🎵➡️🎵

A secure and user-friendly CLI tool for transferring Spotify playlists and liked songs between accounts.

![Demo](https://via.placeholder.com/800x400.png?text=Spotify+Transfer+Tool+Demo)

## Features ✨

- 🔐 Secure credential storage using system keyring
- 🎨 Beautiful terminal interface with Rich
- 🔄 Transfer playlists and liked songs
- ⚡ Smart caching for faster subsequent runs
- ❓ Interactive conflict resolution
- 📊 Progress tracking and status updates

## Installation 📦

```bash
pip install spotify-transfer-tool
```

## Setup Guide ⚙️

### 1. Create Spotify Developer Application
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Click "Create App"
3. Fill in details:
   - **Name**: Transfer Tool
   - **Description**: Personal use
4. Add Redirect URI: `http://localhost:8888/callback`
5. Note your Client ID and Client Secret

### 2. Configure the Tool
```bash
spotify-transfer setup
```
Follow the prompts to enter:
- Client ID
- Client Secret
- Redirect URI (use default)

## Usage 🚀

### Basic Transfer
```bash
spotify-transfer transfer
```

### Options
```bash
# Reuse previous authentication
spotify-transfer transfer --reuse

# Re-authenticate specific account
spotify-transfer transfer --change-account source
```

### Command Help
```bash
spotify-transfer --help
```

## Common Issues ⚠️

### Authentication Errors
- Ensure correct redirect URI matches Spotify Dashboard
- If getting "invalid client" error, re-run `setup`

### Missing Playlists
- Only transfers playlists you own
- Check Spotify API permissions

### Rate Limits
- Tool automatically handles rate limits
- If seeing 429 errors, wait 5 minutes and retry

## Support ❤️

For issues and feature requests:
- [GitHub Issues](https://github.com/yourrepo/issues)

## License 📄

MIT License - See [LICENSE](LICENSE) for details