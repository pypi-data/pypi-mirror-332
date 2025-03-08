"""Command-line interface for the mildmouse package."""

import argparse
import json
import sys
import logging
from .config import (
    load_environment_variables,
    create_env_sample,
    create_env_file,
    get_credentials,
    setup_logging,
    get_config_paths,
)
from .search import search_google
from .formatter import pretty_print_results
from .cache import get_cache_path

logger = logging.getLogger(__name__)


def search_command(args):
    """
    Execute the search command.
    Args:
        args: Parsed arguments namespace
    """
    # Set up default credentials now, after env has been loaded
    credentials = get_credentials()
    if args.key is None:
        args.key = credentials[0]
    if args.cx is None:
        args.cx = credentials[1]

    # Join query terms if provided as separate arguments
    query = " ".join(args.query) if args.query else ""

    # Check for required parameters
    if not query:
        print("Error: Search query is required")
        return 1
    if not args.key:
        print(
            "Error: Google API key is required (use --key or set GOOGLE_API_KEY env variable)"
        )
        print("Use 'mildmouse config --create-sample' to create a sample .env file")
        print("See README.md for setup instructions")
        return 1
    if not args.cx:
        print(
            "Error: Custom Search Engine ID is required (use --cx or set GOOGLE_SEARCH_CX env variable)"
        )
        print("Use 'mildmouse config --create-sample' to create a sample .env file")
        print("See README.md for setup instructions")
        return 1

    logger.info(f"Searching for: {query}")
    try:
        # Perform search
        results = search_google(
            query=query,
            api_key=args.key,
            cx=args.cx,
            num=args.num,
            start=args.start,
            ignore_cache=args.no_cache,
            cache_max_age=args.cache_age,
        )

        # Output results
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            pretty_print_results(results)

        return 0
    except Exception as e:
        logger.error(f"Error during search: {str(e)}")
        print(f"Error: {e}", file=sys.stderr)
        return 1


def config_command(args):
    """
    Execute the config command.
    Args:
        args: Parsed arguments namespace
    """
    # Handle --list flag
    if args.list:
        paths = get_config_paths()
        print("Configuration paths:")
        for name, path in paths.items():
            print(f"  {name}: {path}")
            print(f"    (exists: {path.exists()})")

        # Also show cache file
        cache_path = get_cache_path()
        print(f"  cache_file: {cache_path}")
        print(f"    (exists: {cache_path.exists()})")

        return 0

    # Handle --create-sample flag
    if args.create_sample:
        # Use user config dir by default for --create-sample
        # unless explicitly set to false
        in_user_config = True
        if hasattr(args, "user_config") and args.user_config is False:
            in_user_config = False

        env_sample_path = create_env_sample(in_user_config)
        if in_user_config:
            # Get the path for the actual .env file in the same directory
            config_dir = env_sample_path.parent
            env_file_path = config_dir / ".env"
            print(f"Created sample environment file at {env_sample_path}")
            print(f"Copy or rename this file to {env_file_path}")
            print("Fill in your API key and Search Engine ID")
        else:
            print(f"Created sample environment file at {env_sample_path}")
            print("Copy this to .env and fill in your API key and Search Engine ID")

        print("See README.md for detailed setup instructions")
        return 0

    # Handle --create flag
    if args.create:
        if not args.key or not args.cx:
            print("Error: --create requires both --key and --cx to be provided")
            return 1

        # Use user config dir by default for --create
        # unless explicitly set to false
        in_user_config = True
        if hasattr(args, "user_config") and args.user_config is False:
            in_user_config = False

        env_path = create_env_file(args.key, args.cx, in_user_config)
        print(f"Created .env file at {env_path} with your credentials")
        return 0

    # If no specific action is specified, show the current config
    api_key, cx = get_credentials()
    key_status = "Set" if api_key else "Not set"
    cx_status = "Set" if cx else "Not set"

    paths = get_config_paths()
    print("Current configuration:")
    print(f"  GOOGLE_API_KEY: {key_status}")
    print(f"  GOOGLE_SEARCH_CX: {cx_status}")

    print("\nConfiguration files:")
    for name, path in paths.items():
        if "env_file" in name:  # Only show .env files, not directories
            print(f"  {name}: {path}")
            print(f"    (exists: {path.exists()})")

    return 0


def setup_parsers():
    """
    Set up command-line argument parsers.
    Returns:
        main_parser: The main argument parser
    """
    # Create main parser
    main_parser = argparse.ArgumentParser(
        description="Google Custom Search Engine command-line client"
    )
    main_parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Increase verbosity (-v for info, -v -v for debug)",
    )

    # Create subparsers
    subparsers = main_parser.add_subparsers(dest="command", help="Command to execute")

    # Search command
    search_parser = subparsers.add_parser(
        "search", help="Search Google Custom Search Engine"
    )
    search_parser.add_argument(
        "query", nargs="*", help="Search query (use quotes for multi-word queries)"
    )
    search_parser.add_argument(
        "--key",
        "-k",
        help="Google API key (can also be set via GOOGLE_API_KEY env variable)",
    )
    search_parser.add_argument(
        "--cx",
        "-c",
        help="Custom Search Engine ID (can also be set via GOOGLE_SEARCH_CX env variable)",
    )
    search_parser.add_argument(
        "--num",
        "-n",
        type=int,
        default=10,
        help="Number of results to return (max 10, default: 10)",
    )
    search_parser.add_argument(
        "--start",
        "-s",
        type=int,
        default=1,
        help="Index of first result (1-based, default: 1)",
    )
    search_parser.add_argument(
        "--json", "-j", action="store_true", help="Output results as JSON"
    )
    search_parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Ignore cache and force a fresh API request",
    )
    search_parser.add_argument(
        "--cache-age",
        type=int,
        default=86400,
        help="Maximum age of cached results in seconds (default: 24 hours)",
    )

    # Config command
    config_parser = subparsers.add_parser(
        "config", help="Manage configuration settings"
    )
    config_parser.add_argument(
        "--list", "-l", action="store_true", help="List all configuration paths"
    )
    config_parser.add_argument(
        "--create-sample", action="store_true", help="Create a sample .env.sample file"
    )
    config_parser.add_argument(
        "--create",
        action="store_true",
        help="Create .env file with provided credentials (requires --key and --cx)",
    )
    config_parser.add_argument("--key", "-k", help="Google API key for --create")
    config_parser.add_argument(
        "--cx", "-c", help="Custom Search Engine ID for --create"
    )
    config_parser.add_argument(
        "--local",
        action="store_false",
        dest="user_config",
        help="Use current directory instead of user config directory for file operations",
    )

    return main_parser


def main() -> int:
    """
    Run the command-line interface.
    Returns:
        int: Exit code (0 for success, non-zero for error)
    """
    # Set up parsers
    parser = setup_parsers()

    # Parse arguments
    args = parser.parse_args()

    # Set up logging based on verbosity level
    setup_logging(args.verbose)
    logger.debug(f"Starting mildmouse with arguments: {args}")

    # Load environment variables ONLY from .env, never from .env.sample
    load_environment_variables()
    logger.debug("Environment variables loaded")

    # Handle commands
    if args.command == "search":
        return search_command(args)
    elif args.command == "config":
        return config_command(args)
    else:
        # If no command specified, default to showing help
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
