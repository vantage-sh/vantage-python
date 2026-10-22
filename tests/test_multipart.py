"""CSV uploads use real multipart encoding without making network requests."""

from email import policy
from email.parser import BytesParser
from io import BytesIO

import httpx
import pytest

from vantage import AsyncClient, Client

CSV = b"date,amount\n2026-10-01,12.34\n"
ROUTES = [
    ("POST", "/v2/exchange_rates/csv", None),
    ("PUT", "/v2/business_metrics/metric/values.csv", "forecasted"),
    ("POST", "/v2/integrations/integration/costs.csv", "auto_transform"),
]


def upload_body(kind, flag):
    value = {
        "bytes": lambda: CSV,
        "stream": lambda: BytesIO(CSV),
        "tuple": lambda: ("costs.csv", CSV, "text/csv"),
        "text": lambda: CSV.decode(),
    }[kind]()
    return {"csv": value, **({flag: False} if flag else {})}


def verify_upload(request, method, path, flag):
    assert request.method == method
    assert request.url.path == path
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    message = BytesParser(policy=policy.default).parsebytes(
        b"Content-Type: "
        + request.headers["Content-Type"].encode()
        + b"\r\n\r\n"
        + request.content
    )
    parts = {
        part.get_param("name", header="content-disposition"): part
        for part in message.iter_parts()
    }
    assert parts["csv"].get_filename()
    assert parts["csv"].get_payload(decode=True) == CSV
    if flag:
        assert parts[flag].get_payload(decode=True) == b"false"
    return httpx.Response(204)


@pytest.mark.parametrize("method,path,flag", ROUTES)
@pytest.mark.parametrize("kind", ["bytes", "stream", "tuple", "text"])
def test_sync_csv_upload(method, path, flag, kind):
    body = upload_body(kind, flag)
    original = dict(body)
    with Client("test-token", base_url="https://vantage.invalid") as client:
        client._http.close()
        client._http = httpx.Client(
            transport=httpx.MockTransport(
                lambda request: verify_upload(request, method, path, flag)
            )
        )
        client.request(method, path, body=body)
    assert body == original


@pytest.mark.parametrize("method,path,flag", ROUTES)
@pytest.mark.parametrize("kind", ["bytes", "stream", "tuple", "text"])
async def test_async_csv_upload(method, path, flag, kind):
    body = upload_body(kind, flag)
    original = dict(body)
    async with AsyncClient("test-token", base_url="https://vantage.invalid") as client:
        await client._http.aclose()
        client._http = httpx.AsyncClient(
            transport=httpx.MockTransport(
                lambda request: verify_upload(request, method, path, flag)
            )
        )
        await client.request(method, path, body=body)
    assert body == original


@pytest.mark.parametrize("method", ["GET", "POST"])
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_non_upload_requests(method, asynchronous):
    import json

    def handle(request):
        assert request.method == method
        if method == "GET":
            assert request.url.params["name"] == "a & b"
        else:
            assert request.headers["Content-Type"] == "application/json"
            assert json.loads(request.content) == {"name": "a & b"}
        return httpx.Response(200, json={"ok": True})

    kwargs = (
        {"params": {"name": "a & b"}}
        if method == "GET"
        else {"body": {"name": "a & b"}}
    )
    if asynchronous:
        async with AsyncClient(
            "test-token", base_url="https://vantage.invalid"
        ) as client:
            await client._http.aclose()
            client._http = httpx.AsyncClient(transport=httpx.MockTransport(handle))
            assert await client.request(method, "/v2/workspaces", **kwargs) == {
                "ok": True
            }
    else:
        with Client("test-token", base_url="https://vantage.invalid") as client:
            client._http.close()
            client._http = httpx.Client(transport=httpx.MockTransport(handle))
            assert client.request(method, "/v2/workspaces", **kwargs) == {"ok": True}


@pytest.mark.parametrize("mode", ["sync", "async"])
def test_generated_upload_matches_checked_in_client(mode):
    import ast
    import importlib.util
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location(
        "vantage_autogen", root / "autogen.py"
    )
    generator = importlib.util.module_from_spec(spec)
    import sys

    sys.modules[spec.name] = generator
    spec.loader.exec_module(generator)
    generated = getattr(generator, f"generate_{mode}_client")({})
    checked_in = (root / "src" / "vantage" / f"_{mode}" / "client.py").read_text()

    def request_ast(source):
        return ast.dump(
            next(
                node
                for node in ast.walk(ast.parse(source))
                if isinstance(node, ast.If)
                and isinstance(node.test, ast.Call)
                and isinstance(node.test.func, ast.Name)
                and node.test.func.id == "is_multipart_route"
            )
        )

    assert request_ast(generated) == request_ast(checked_in)
