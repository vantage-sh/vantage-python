"""
Vantage API Python SDK.

This package provides both synchronous and asynchronous clients for the Vantage API.

Usage:
    # Synchronous client
    from vantage import Client

    client = Client("your-api-token")
    folders = client.folders.list()

    # Async client
    from vantage import AsyncClient

    async def main():
        async with AsyncClient("your-api-token") as client:
            folders = await client.folders.list()

    # Never-throw mode (Go-style error handling)
    client = Client("your-api-token", never_throw=True)
    result = client.folders.list()
    if result.ok:
        print(result.value)
    else:
        print(result.error)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ._base import VantageAPIError, Result, DEFAULT_BASE_URL

if TYPE_CHECKING:
    from ._sync.client import SyncClient
    from ._async.client import AsyncClient as _AsyncClient

__all__ = [
    "Client",
    "AsyncClient",
    "VantageAPIError",
    "Result",
    "DEFAULT_BASE_URL",
]


def Client(
    bearer_token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    never_throw: bool = False,
) -> "SyncClient":
    """
    Create a synchronous Vantage API client.

    Args:
        bearer_token: Your Vantage API bearer token.
        base_url: Base URL for the API (default: https://api.vantage.sh).
        never_throw: If True, returns Result objects instead of raising exceptions.

    Returns:
        A synchronous client instance.

    Example:
        client = Client("your-token")
        folders = client.folders.list()
    """
    from ._sync.client import SyncClient

    return SyncClient(bearer_token, base_url=base_url, never_throw=never_throw)


def AsyncClient(
    bearer_token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    never_throw: bool = False,
) -> "_AsyncClient":
    """
    Create an asynchronous Vantage API client.

    Args:
        bearer_token: Your Vantage API bearer token.
        base_url: Base URL for the API (default: https://api.vantage.sh).
        never_throw: If True, returns Result objects instead of raising exceptions.

    Returns:
        An asynchronous client instance.

    Example:
        async with AsyncClient("your-token") as client:
            folders = await client.folders.list()
    """
    from ._async.client import AsyncClient as _AsyncClientImpl

    return _AsyncClientImpl(bearer_token, base_url=base_url, never_throw=never_throw)
