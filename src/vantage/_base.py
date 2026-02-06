"""Base client implementation for Vantage API."""

from __future__ import annotations

from typing import Any, TypeVar, Generic, Optional, List, Dict, Set
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class VantageAPIError(Exception):
    """Error returned from the Vantage API."""

    status: Optional[int]
    status_text: Optional[str]
    body: str
    errors: Optional[List[str]] = None

    def __post_init__(self) -> None:
        super().__init__(f"VantageAPIError: {self.status} {self.status_text}")
        # Try to parse errors from JSON body
        if self.body:
            try:
                import json

                parsed = json.loads(self.body)
                if isinstance(parsed, dict) and "errors" in parsed:
                    self.errors = parsed["errors"]
            except (json.JSONDecodeError, KeyError):
                pass


@dataclass
class Result(Generic[T]):
    """Result wrapper for never-throw mode."""

    value: Optional[T] = None
    error: Optional[VantageAPIError] = None

    @property
    def ok(self) -> bool:
        return self.error is None

    def unwrap(self) -> T:
        if self.error is not None:
            raise self.error
        return self.value  # type: ignore


# Multipart edge cases - routes that use multipart/form-data
MULTIPART_ROUTES: Dict[str, Set[str]] = {
    "/v2/exchange_rates/csv": {"POST"},
    "/v2/business_metrics/{business_metric_token}/values.csv": {"PUT"},
    "/v2/integrations/{integration_token}/costs.csv": {"POST"},
}


def is_multipart_route(path: str, method: str) -> bool:
    """Check if a route uses multipart/form-data."""
    import re

    for pattern, methods in MULTIPART_ROUTES.items():
        if method.upper() not in methods:
            continue
        # Convert path pattern to regex
        regex_pattern = re.sub(r"\{[^}]+\}", r"[^/]+", pattern)
        if re.fullmatch(regex_pattern, path):
            return True
    return False


def build_query_string(params: Dict[str, Any]) -> str:
    """Build a query string from parameters."""
    if not params:
        return ""
    parts = []
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            parts.append(f"{key}={str(value).lower()}")
        elif isinstance(value, list):
            parts.append(f"{key}={','.join(str(v) for v in value)}")
        else:
            parts.append(f"{key}={value}")
    return "?" + "&".join(parts) if parts else ""


DEFAULT_BASE_URL = "https://api.vantage.sh/v2"
