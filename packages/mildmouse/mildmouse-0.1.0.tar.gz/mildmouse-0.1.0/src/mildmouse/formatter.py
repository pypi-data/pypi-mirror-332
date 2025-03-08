"""Formatting utilities for search results."""

from typing import Any, Dict, List


def format_search_results(results: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    Format Google search results into a simplified list.

    Args:
        results: Response from the Google Custom Search API

    Returns:
        List of dictionaries with title, link, and snippet
    """
    formatted_results = []

    if "items" not in results:
        return formatted_results

    for item in results.get("items", []):
        formatted_results.append(
            {
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "snippet": item.get("snippet", ""),
            }
        )

    return formatted_results


def pretty_print_results(results: Dict[str, Any]) -> None:
    """
    Print search results in a human-readable format.

    Args:
        results: Response from the Google Custom Search API
    """
    if "items" not in results:
        print("No results found.")
        return

    print(
        f"About {results.get('searchInformation', {}).get('formattedTotalResults', '0')} results "
        f"({results.get('searchInformation', {}).get('formattedSearchTime', '0')} seconds)"
    )
    print("-" * 80)

    for i, item in enumerate(results.get("items", []), 1):
        print(f"{i}. {item.get('title', '')}")
        print(f"   {item.get('link', '')}")
        print(f"   {item.get('snippet', '')}")
        print()
