# mildmouse

A command-line tool for querying Google Custom Search Engine.

## Installation

```bash
pip install mildmouse
```

## Setup

### 1. Get a Google API Key

a. Go to https://console.cloud.google.com/
b. Create a new project (or select an existing one)
c. Navigate to 'APIs & Services' > 'Library'
d. Search for 'Custom Search API' and enable it
e. Go to 'APIs & Services' > 'Credentials'
f. Click 'Create Credentials' > 'API Key'
g. Copy your new API key

### 2. Create a Custom Search Engine

a. Go to https://programmablesearchengine.google.com/
b. Click 'Add' to create a new search engine
c. Configure your search engine (select sites to search or 'Search the entire web')
d. After creation, click 'Control Panel'
e. Navigate to the 'Setup' or 'Basics' section
f. Find your 'Search engine ID' (cx) value

### 3. Configure mildmouse

#### Option 1: Use environment variables directly
```bash
export GOOGLE_API_KEY=your_api_key_here
export GOOGLE_SEARCH_CX=your_search_engine_id_here
```

#### Option 2: Create a .env file
```bash
# Create a template to see the format (creates in user config directory by default)
mildmouse config --create-sample

# Create in current directory instead
mildmouse config --create-sample --local

# Or create directly with your credentials (creates in user config directory by default)
mildmouse config --create --key YOUR_API_KEY --cx YOUR_CX_ID

# Create in current directory instead
mildmouse config --create --key YOUR_API_KEY --cx YOUR_CX_ID --local
```

## Usage

### Search

Basic search:
```bash
mildmouse search "your search query"
```

Specify API key and Search Engine ID:
```bash
mildmouse search "your search query" --key YOUR_API_KEY --cx YOUR_CX_ID
```

Get JSON output:
```bash
mildmouse search "your search query" --json
```

Get more results (max 10):
```bash
mildmouse search "your search query" --num 10
```

Start from a specific result:
```bash
mildmouse search "your search query" --start 11
```

### Configuration

View current configuration:
```bash
mildmouse config
```

List all configuration paths:
```bash
mildmouse config --list
```

Create a sample configuration file:
```bash
mildmouse config --create-sample      # In user config directory
mildmouse config --create-sample --local  # In current directory
```

Create a configuration file with your credentials:
```bash
mildmouse config --create --key YOUR_API_KEY --cx YOUR_CX_ID      # In user config directory
mildmouse config --create --key YOUR_API_KEY --cx YOUR_CX_ID --local  # In current directory
```

### Logging

Enable verbose logging:
```bash
mildmouse -v search "your search query"       # Info level logging
mildmouse -v -v search "your search query"    # Debug level logging
```

## Environment Variables

The following environment variables can be set:

- `GOOGLE_API_KEY`: Your Google API key
- `GOOGLE_SEARCH_CX`: Your Custom Search Engine ID

## Configuration Locations

The tool checks for .env files in the following locations (in order of priority):
1. Current directory (./.env)
2. User config directory (platform specific):
   - Linux: ~/.config/mildmouse/.env
   - macOS: ~/Library/Application Support/mildmouse/.env
   - Windows: C:\Users\<username>\AppData\Roaming\mildmouse\.env
3. Home directory (~/.env)

## License

[MIT](LICENSE)
```

I've made several important changes:

1. **Reversed the default behavior for file creation**:
   - Now creates files in the user config directory by default
   - Added a `--local` flag to create files in the current directory instead
   - This is more in line with modern application design practices

2. **Fixed the config command's behavior**:
   - Modified `config_command()` to use the user config directory by default
   - Added logic to check if `user_config` was explicitly set to False

3. **Updated CLI argument design**:
   - Changed from `--user-config` to `--local`, which better explains what it does
   - Set `dest="user_config"` and `action="store_false"` to reverse the logic

4. **Updated README**:
   - Clarified the new default behavior
   - Added examples showing both user config and local directory usage
   - Added more details about the platform-specific paths

The key change is that configurations are now created in the user's config directory by default (e.g., `~/Library/Application Support/mildmouse/.env` on macOS), and you need to use `--local` flag if you want to use the current directory instead.
