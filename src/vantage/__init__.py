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
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ._base import VantageAPIError, DEFAULT_BASE_URL
from ._types import *

if TYPE_CHECKING:
    from ._sync.client import SyncClient as _SyncClient
    from ._async.client import AsyncClient as _AsyncClient


def Client(
    bearer_token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
) -> "_SyncClient":
    """
    Create a synchronous Vantage API client.

    Args:
        bearer_token: Your Vantage API bearer token.
        base_url: Base URL for the API (default: https://api.vantage.sh).

    Returns:
        A synchronous client instance.

    Example:
        client = Client("your-token")
        folders = client.folders.list()
    """
    from ._sync.client import SyncClient

    return SyncClient(bearer_token, base_url=base_url)


def AsyncClient(
    bearer_token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
) -> "_AsyncClient":
    """
    Create an asynchronous Vantage API client.

    Args:
        bearer_token: Your Vantage API bearer token.
        base_url: Base URL for the API (default: https://api.vantage.sh).

    Returns:
        An asynchronous client instance.

    Example:
        async with AsyncClient("your-token") as client:
            folders = await client.folders.list()
    """
    from ._async.client import AsyncClient as _AsyncClientImpl

    return _AsyncClientImpl(bearer_token, base_url=base_url)
