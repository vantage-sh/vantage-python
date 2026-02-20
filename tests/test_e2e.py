"""End-to-end tests for the Vantage API SDK.

Requires VANTAGE_API_TOKEN and VANTAGE_WORKSPACE_TOKEN environment variables.
Tests the full CRUD lifecycle on folders using both sync and async clients.
"""

from __future__ import annotations

import os

import pytest

from vantage import Client, AsyncClient, VantageAPIError
from vantage._types import CreateFolder, UpdateFolder

API_TOKEN = os.environ.get("VANTAGE_API_TOKEN", "")
WORKSPACE_TOKEN = os.environ.get("VANTAGE_WORKSPACE_TOKEN", "")

pytestmark = pytest.mark.skipif(
    not API_TOKEN or not WORKSPACE_TOKEN,
    reason="VANTAGE_API_TOKEN and VANTAGE_WORKSPACE_TOKEN required",
)


# ── Sync client ──────────────────────────────────────────────────────────────


class TestSyncCRUD:
    """Full folder CRUD lifecycle with the synchronous client."""

    def test_lifecycle(self) -> None:
        client = Client(API_TOKEN)

        # Create
        folder = client.folders.create(
            CreateFolder(title="E2E Test Folder", workspace_token=WORKSPACE_TOKEN)
        )
        assert folder.title == "E2E Test Folder"
        token = folder.token

        try:
            # Read
            fetched = client.folders.get(token)
            assert fetched.title == "E2E Test Folder"

            # Update
            updated = client.folders.update(
                token, UpdateFolder(title="Updated E2E Folder")
            )
            assert updated.title == "Updated E2E Folder"
        finally:
            # Delete
            client.folders.delete(token)


class TestSyncErrors:
    """Error handling with the synchronous client."""

    def test_bad_token_raises(self) -> None:
        client = Client("bad")
        with pytest.raises(VantageAPIError) as exc_info:
            client.folders.list()
        assert exc_info.value.status == 401


# ── Async client ─────────────────────────────────────────────────────────────


class TestAsyncCRUD:
    """Full folder CRUD lifecycle with the asynchronous client."""

    async def test_lifecycle(self) -> None:
        async with AsyncClient(API_TOKEN) as client:
            # Create
            folder = await client.folders.create(
                CreateFolder(title="E2E Async Test Folder", workspace_token=WORKSPACE_TOKEN)
            )
            assert folder.title == "E2E Async Test Folder"
            token = folder.token

            try:
                # Read
                fetched = await client.folders.get(token)
                assert fetched.title == "E2E Async Test Folder"

                # Update
                updated = await client.folders.update(
                    token, UpdateFolder(title="Updated E2E Async Folder")
                )
                assert updated.title == "Updated E2E Async Folder"
            finally:
                # Delete
                await client.folders.delete(token)


class TestAsyncErrors:
    """Error handling with the asynchronous client."""

    async def test_bad_token_raises(self) -> None:
        async with AsyncClient("bad") as client:
            with pytest.raises(VantageAPIError) as exc_info:
                await client.folders.list()
            assert exc_info.value.status == 401
