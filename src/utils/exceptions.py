class FrameworkError(Exception):
    """Base exception for the QA automation framework."""


class ConfigError(FrameworkError):
    """Raised when configuration is invalid or missing."""


class TestDataError(FrameworkError):
    """Raised when test data is invalid or cannot be loaded."""


class ApiClientError(FrameworkError):
    """Raised when API client operation fails."""


class ResponseValidationError(FrameworkError):
    """Raised when API response validation fails."""