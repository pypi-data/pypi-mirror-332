"""Custom exceptions for the mildmouse package."""


class SearchError(Exception):
    """Exception raised for errors during the search process."""

    pass


class APIError(SearchError):
    """Exception raised for errors from the Google API."""

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error ({status_code}): {message}")


class ConfigError(Exception):
    """Exception raised for configuration errors."""

    pass
