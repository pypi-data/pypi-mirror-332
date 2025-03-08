"""Google Custom Search Engine API interface."""

import json
import logging
import urllib.request
import urllib.parse
import urllib.error
from typing import Any, Dict, Optional

from .cache import get_from_cache, save_to_cache

logger = logging.getLogger(__name__)


def search_google(
    query: str,
    api_key: str,
    cx: str,
    start: int = 1,
    num: int = 10,
    safe: str = "off",
    fields: Optional[str] = None,
    ignore_cache: bool = False,
    cache_max_age: int = 86400,
) -> Dict[str, Any]:
    """
    Search Google using the Custom Search JSON API.
    Args:
        query: Search query string
        api_key: Google API key
        cx: Custom Search Engine ID
        start: Index of first result (1-based, default: 1)
        num: Number of results to return (max 10, default: 10)
        safe: Safe search level ('off', 'medium', 'high', default: 'off')
        fields: Comma-separated list of fields to include in the response
        ignore_cache: If True, bypass the cache and force a fresh API request
        cache_max_age: Maximum age of cached results in seconds (default: 24 hours)
    Returns:
        Dict containing the search results
    """
    # Try to get from cache first if not ignoring cache
    cached_results, from_cache = get_from_cache(
        query,
        cx,
        start,
        num,
        safe,
        fields,
        max_age=cache_max_age,
        ignore_cache=ignore_cache,
    )

    if from_cache:
        return cached_results

    # If not in cache or ignoring cache, perform the search
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
        "start": start,
        "num": num,
        "safe": safe,
    }
    if fields:
        params["fields"] = fields
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    # Log request (with API key partially masked)
    masked_params = params.copy()
    if masked_params.get("key"):
        key = masked_params["key"]
        if len(key) > 8:
            masked_params["key"] = key[:4] + "..." + key[-4:]
        else:
            masked_params["key"] = "****"
    logger.info("Sending request to Google Custom Search API")
    logger.debug(f"Request URL: {base_url}")
    logger.debug(f"Request parameters: {masked_params}")

    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            response_data = response.read().decode("utf-8")
            result = json.loads(response_data)
            logger.info(f"Received response with status: {response.status}")
            logger.debug(f"Response headers: {dict(response.getheaders())}")
            logger.debug(f"Response JSON: {json.dumps(result, indent=2)}")

            # Save to cache if successful
            save_to_cache(query, cx, start, num, safe, fields, result)

            return result
    except urllib.error.HTTPError as e:
        error_message = e.read().decode("utf-8")
        logger.error(f"HTTP Error {e.code}: {error_message}")
        raise RuntimeError(f"HTTP Error {e.code}: {error_message}")
    except Exception as e:
        logger.error(f"Error during API request: {str(e)}")
        raise
