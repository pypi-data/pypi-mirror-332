"""Cache handling for search results."""

import json
import logging
import os
import time
from pathlib import Path
from platformdirs import user_config_dir

logger = logging.getLogger(__name__)
APP_NAME = "mildmouse"


def get_cache_path():
    """
    Get the path to the cache file.

    Returns:
        Path: Path to the cache file
    """
    cache_dir = Path(user_config_dir(APP_NAME))
    return cache_dir / "cache.json"


def load_cache():
    """
    Load the cache from disk.

    Returns:
        dict: The cache contents or empty dict if no cache exists
    """
    cache_path = get_cache_path()

    if not cache_path.exists():
        logger.debug(f"No cache file found at {cache_path}")
        return {}

    try:
        with open(cache_path, "r") as f:
            logger.debug(f"Loading cache from {cache_path}")
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"Failed to load cache: {e}")
        return {}


def save_cache(cache):
    """
    Save the cache to disk.

    Args:
        cache (dict): The cache to save
    """
    cache_path = get_cache_path()

    # Ensure directory exists
    os.makedirs(cache_path.parent, exist_ok=True)

    try:
        with open(cache_path, "w") as f:
            logger.debug(f"Saving cache to {cache_path}")
            json.dump(cache, f, indent=2)
    except IOError as e:
        logger.warning(f"Failed to save cache: {e}")


def get_cache_key(query, cx, start, num, safe, fields):
    """
    Generate a cache key for the search parameters.

    Args:
        query (str): Search query
        cx (str): Custom Search Engine ID
        start (int): Starting index
        num (int): Number of results
        safe (str): Safe search setting
        fields (str): Fields to return

    Returns:
        str: Cache key
    """
    # Create a tuple of all parameters that affect the search results
    params = (query, cx, start, num, safe, fields or "")

    # Convert to a string that can be used as a key
    return json.dumps(params, sort_keys=True)


def get_from_cache(
    query, cx, start, num, safe, fields, max_age=86400, ignore_cache=False
):
    """
    Try to get search results from cache.

    Args:
        query (str): Search query
        cx (str): Custom Search Engine ID
        start (int): Starting index
        num (int): Number of results
        safe (str): Safe search setting
        fields (str): Fields to return
        max_age (int): Maximum age of cached results in seconds (default: 24 hours)
        ignore_cache (bool): If True, bypass the cache completely

    Returns:
        tuple: (results, from_cache) where results is the search results (or None if not found)
               and from_cache is a boolean indicating whether the results came from cache
    """
    if ignore_cache:
        logger.info("Cache ignored as requested")
        return None, False

    cache = load_cache()
    cache_key = get_cache_key(query, cx, start, num, safe, fields)

    if cache_key in cache:
        cache_entry = cache[cache_key]
        cache_time = cache_entry.get("timestamp", 0)
        current_time = time.time()

        # Check if cache entry is still valid
        if current_time - cache_time <= max_age:
            logger.info(f"Cache HIT for query: {query}")
            return cache_entry.get("results"), True
        else:
            logger.info(
                f"Cache EXPIRED for query: {query} (age: {int(current_time - cache_time)} seconds)"
            )
    else:
        logger.info(f"Cache MISS for query: {query}")

    return None, False


def save_to_cache(query, cx, start, num, safe, fields, results):
    """
    Save search results to cache.

    Args:
        query (str): Search query
        cx (str): Custom Search Engine ID
        start (int): Starting index
        num (int): Number of results
        safe (str): Safe search setting
        fields (str): Fields to return
        results (dict): Search results to cache
    """
    cache = load_cache()
    cache_key = get_cache_key(query, cx, start, num, safe, fields)

    cache[cache_key] = {"timestamp": time.time(), "results": results}

    save_cache(cache)
    logger.info(f"Saved results to cache for query: {query}")
