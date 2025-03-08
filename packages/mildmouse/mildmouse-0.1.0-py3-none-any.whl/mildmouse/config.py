"""Configuration handling for the mildmouse package."""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from platformdirs import user_config_dir

logger = logging.getLogger(__name__)

APP_NAME = "mildmouse"


def get_config_paths():
    """
    Get paths for config files.

    Returns:
        dict: Paths for various configuration locations
    """
    # Get user config directory
    user_config = Path(user_config_dir(APP_NAME))

    return {
        "user_config_dir": user_config,
        "user_env_file": user_config / ".env",
        "user_env_sample": user_config / ".env.sample",
        "local_env_file": Path.cwd() / ".env",
        "local_env_sample": Path.cwd() / ".env.sample",
        "home_env_file": Path.home() / ".env",
    }


def load_environment_variables():
    """
    Load environment variables from .env files.

    Checks in multiple locations with the following priority:
    1. Current directory
    2. User config directory
    3. Home directory
    """
    paths = get_config_paths()
    env_loaded = False

    # Try loading from current directory first
    if paths["local_env_file"].exists():
        logger.info(f"Loading environment from: {paths['local_env_file']}")
        load_dotenv(paths["local_env_file"])
        env_loaded = True

    # Then try user config directory
    if paths["user_env_file"].exists():
        logger.info(f"Loading environment from: {paths['user_env_file']}")
        load_dotenv(paths["user_env_file"])
        env_loaded = True

    # Finally try home directory
    if paths["home_env_file"].exists():
        logger.info(f"Loading environment from: {paths['home_env_file']}")
        load_dotenv(paths["home_env_file"])
        env_loaded = True

    if not env_loaded:
        logger.warning("No .env file found in any of the standard locations")
        logger.info(
            f"Checked: {paths['local_env_file']}, {paths['user_env_file']}, {paths['home_env_file']}"
        )


def get_credentials():
    """
    Get API credentials from environment variables.

    Returns:
        Tuple of (api_key, cx)
    """
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    cx = os.environ.get("GOOGLE_SEARCH_CX", "")

    # Debug env vars if they're not found
    if not api_key or not cx:
        logger.debug(
            f"Environment variables: GOOGLE_API_KEY={'set' if api_key else 'not set'}, GOOGLE_SEARCH_CX={'set' if cx else 'not set'}"
        )
        # List all env vars for debugging (only at debug level)
        logger.debug(f"All environment variables: {list(os.environ.keys())}")

    return api_key, cx


def create_env_sample(in_user_config=False):
    """
    Create a sample .env file to demonstrate the format.

    Args:
        in_user_config: If True, create in user config dir instead of current dir

    Returns:
        Path to the created file
    """
    paths = get_config_paths()

    if in_user_config:
        # Make sure the directory exists
        os.makedirs(paths["user_config_dir"], exist_ok=True)
        target_path = paths["user_env_sample"]
    else:
        target_path = paths["local_env_sample"]

    with open(target_path, "w") as f:
        f.write("# Google Custom Search Engine credentials\n")
        f.write(
            "# Get your API key from https://developers.google.com/custom-search/v1/overview\n"
        )
        f.write(
            "# Create a custom search engine at https://programmablesearchengine.google.com/\n"
        )
        f.write(
            "# The Search Engine ID (cx) is shown in the 'Setup' section after creation\n"
        )
        f.write("GOOGLE_API_KEY=your_api_key_here\n")
        f.write("GOOGLE_SEARCH_CX=your_search_engine_id_here\n")

    return target_path


def create_env_file(api_key, cx, in_user_config=False):
    """
    Create a .env file with the provided credentials.

    Args:
        api_key: Google API key
        cx: Custom Search Engine ID
        in_user_config: If True, create in user config dir instead of current dir

    Returns:
        Path to the created file
    """
    paths = get_config_paths()

    if in_user_config:
        # Make sure the directory exists
        os.makedirs(paths["user_config_dir"], exist_ok=True)
        target_path = paths["user_env_file"]
    else:
        target_path = paths["local_env_file"]

    with open(target_path, "w") as f:
        f.write("# Google Custom Search Engine credentials\n")
        f.write(f"GOOGLE_API_KEY={api_key}\n")
        f.write(f"GOOGLE_SEARCH_CX={cx}\n")

    return target_path


def setup_logging(verbosity=0):
    """
    Configure logging based on verbosity level.

    Args:
        verbosity: 0=warning, 1=info, 2+=debug
    """
    root_logger = logging.getLogger()

    # Set log level based on verbosity
    if verbosity == 0:
        level = logging.WARNING
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG

    # Configure handler if not already configured
    if not root_logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    root_logger.setLevel(level)

    # Log the logging level being set
    if level == logging.WARNING:
        pass  # Don't log at warning level
    elif level == logging.INFO:
        logging.info("Verbose logging enabled (info level)")
    elif level == logging.DEBUG:
        logging.info("Debug logging enabled (debug level)")
