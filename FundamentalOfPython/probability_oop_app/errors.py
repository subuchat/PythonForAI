class ConfigurationError(Exception):
    """Raised when application configuration is missing or invalid."""


class DistributionError(ValueError):
    """Raised when probability-distribution parameters are invalid."""
