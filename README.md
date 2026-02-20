# vantage-python

A Python SDK for the [Vantage](https://vantage.sh) API. Types and client methods are auto-generated from the official OpenAPI specification.

## Installation

```bash
pip install vantage-python
```

## Usage

### Synchronous Client

```python
from vantage import Client

client = Client("your-api-token")

# List resources with query parameters
reports = client.cost_reports.list(page=1)

# Get a specific resource by token
report = client.cost_reports.get("rprt_abc123")

# Create a new resource
folder = client.folders.create(CreateFolder(
    title="Production Costs",
    workspace_token="wrkspc_123",
))

# Update a resource
client.folders.update("fldr_abc123", UpdateFolder(
    title="Updated Title",
))

# Delete a resource
client.folders.delete("fldr_abc123")
```

### Async Client

```python
from vantage import AsyncClient

async with AsyncClient("your-api-token") as client:
    folders = await client.folders.list()

    folder = await client.folders.create(CreateFolder(
        title="Production Costs",
        workspace_token="wrkspc_123",
    ))
```

## Error Handling

API errors are raised as `VantageAPIError` with structured error information:

```python
from vantage import Client, VantageAPIError

try:
    client.cost_reports.get("invalid_token")
except VantageAPIError as e:
    print(e.status)      # 404
    print(e.status_text)  # "Not Found"
    print(e.errors)       # ["Resource not found"] or None
```

## Development

### Building

```bash
make install
```

This generates Pydantic models, sync client, and the async client. Your pip version will need to be up to date for this. If you wish to generate the client first, you should use `make generate`.

### Testing

```bash
pytest
```

### Publishing

```bash
make publish
```
