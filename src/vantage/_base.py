"""Base client implementation for Vantage API."""

from __future__ import annotations

from typing import Any, Optional, List, Dict, Set
from dataclasses import dataclass
from urllib.parse import quote


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
    """Build a URL-safe query string from parameters."""
    if not params:
        return ""
    parts = []
    for key, value in params.items():
        if value is None:
            continue
        enc_key = quote(str(key), safe="")
        if isinstance(value, bool):
            parts.append(f"{enc_key}={str(value).lower()}")
        elif isinstance(value, list):
            joined = ",".join(quote(str(v), safe="") for v in value)
            parts.append(f"{enc_key}={joined}")
        else:
            parts.append(f"{enc_key}={quote(str(value), safe='')}")
    return "?" + "&".join(parts) if parts else ""


DEFAULT_BASE_URL = "https://api.vantage.sh"
