#!/usr/bin/env python3
"""
Code generator for Vantage API SDK.

Fetches the OpenAPI schema from the Vantage API and generates:
- Type definitions (Pydantic models)
- Sync client
- Async client
"""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

OPENAPI_URL = "https://api.vantage.sh/v2/oas_v3.json"
OUTPUT_DIR = Path(__file__).parent / "src" / "vantage"


@dataclass
class Parameter:
    """OpenAPI parameter definition."""

    name: str
    location: str  # path, query, header
    required: bool
    python_name: str
    param_type: str = "str"
    description: str | None = None


@dataclass
class Endpoint:
    """OpenAPI endpoint definition."""

    path: str
    method: str
    operation_id: str
    summary: str | None
    description: str | None
    deprecated: bool
    parameters: list[Parameter] = field(default_factory=list)
    request_body_required: bool = False
    request_body_type: str | None = None
    response_type: str | None = None
    is_multipart: bool = False


@dataclass
class Resource:
    """API resource grouping."""

    name: str
    endpoints: list[Endpoint] = field(default_factory=list)


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


# Python names that collide with BaseModel attributes or builtins
RESERVED_FIELD_NAMES = frozenset({
    "schema", "validate", "model_fields", "model_computed_fields",
    "model_config", "model_post_init", "model_dump", "model_json_schema",
    "model_rebuild", "model_validate", "model_validate_json",
})


def sanitize_python_name(name: str) -> str:
    """Convert a parameter name to a valid Python identifier."""
    # Handle bracket notation: settings[include_credits] -> settings_include_credits
    name = re.sub(r"\[([^\]]+)\]", r"_\1", name)
    # Replace any remaining non-alphanumeric chars with underscore
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    # Convert to snake_case
    name = to_snake_case(name)
    # Remove leading/trailing underscores
    name = name.strip("_")
    # Ensure it doesn't start with a number
    if name and name[0].isdigit():
        name = "_" + name
    return name


def sanitize_docstring(text: str | None) -> str | None:
    """Clean up text for use in docstrings."""
    if not text:
        return text
    # Replace newlines with spaces, collapse multiple spaces
    text = " ".join(text.split())
    return text


def to_pascal_case(name: str) -> str:
    """Convert snake_case or camelCase to PascalCase."""
    # Normalize to snake_case first to handle camelCase input,
    # then capitalize each segment. Using .capitalize() after
    # snake_case splitting avoids .title() lowering inner chars
    # (e.g. "accessGrant" -> "access_grant" -> "AccessGrant"
    #  instead of "accessGrant" -> "Accessgrant").
    snake = to_snake_case(name)
    return "".join(word.capitalize() for word in snake.replace("-", "_").split("_") if word)


def preprocess_inline_models(schemas: dict[str, Any]) -> None:
    """
    Scan all schema properties for inline objects with explicit properties
    that don't match any existing named schema. Create synthetic schema
    entries so they get proper Pydantic models instead of Dict[str, Any].

    Naming rules:
    - Default name: PascalCase of the property key (e.g. settings -> Settings)
    - If that conflicts with an existing schema or another inline group with
      different keys, prefix with parent model name(s) joined by 'Or'.
    """
    existing_names = {to_pascal_case(name) for name in schemas}

    # Phase 1: Collect inline objects that don't match existing schemas
    # candidate_name -> [(parent_schema_name, sorted_keys, prop_spec)]
    candidates: dict[str, list[tuple[str, tuple[str, ...], dict[str, Any]]]] = {}

    for schema_name in list(schemas):
        for prop_name, prop_spec in schemas[schema_name].get("properties", {}).items():
            if prop_spec.get("type") != "object":
                continue
            if prop_spec.get("additionalProperties"):
                continue
            inline_props = prop_spec.get("properties")
            if not inline_props:
                continue

            inline_keys = tuple(sorted(inline_props.keys()))
            if any(
                tuple(sorted(sd.get("properties", {}).keys())) == inline_keys
                for sd in schemas.values()
                if sd.get("properties")
            ):
                continue

            cand = to_pascal_case(prop_name)
            candidates.setdefault(cand, []).append((schema_name, inline_keys, prop_spec))

    # Phase 2: Resolve names and add synthetic schemas
    for cand_name, instances in candidates.items():
        # Group by key structure
        by_keys: dict[tuple[str, ...], list[tuple[str, dict[str, Any]]]] = {}
        for parent, keys, spec in instances:
            by_keys.setdefault(keys, []).append((parent, spec))

        needs_prefix = cand_name in existing_names or len(by_keys) > 1

        for keys, group in by_keys.items():
            if needs_prefix:
                parents = sorted({to_pascal_case(p) for p, _ in group})
                model_name = "Or".join(parents) + cand_name
            else:
                model_name = cand_name

            # Pick the spec with the most documentation (descriptions + defaults)
            best = max(
                (s for _, s in group),
                key=lambda s: sum(
                    bool(v.get("description")) + ("default" in v)
                    for v in s.get("properties", {}).values()
                ),
            )

            synthetic: dict[str, Any] = {
                "type": "object",
                "properties": best["properties"],
            }
            for k in ("required", "description"):
                if best.get(k):
                    synthetic[k] = best[k]

            schemas[model_name] = synthetic
            existing_names.add(model_name)


def openapi_type_to_python(schema: dict[str, Any], schemas: dict[str, Any]) -> str:
    """Convert OpenAPI type to Python type hint."""
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return to_pascal_case(ref_name)

    schema_type = schema.get("type", "any")

    if schema_type == "string":
        if schema.get("format") == "date-time":
            return "str"  # Keep as string, could use datetime
        return "str"
    elif schema_type == "integer":
        return "int"
    elif schema_type == "number":
        return "float"
    elif schema_type == "boolean":
        return "bool"
    elif schema_type == "array":
        items = schema.get("items", {})
        item_type = openapi_type_to_python(items, schemas)
        return f"List[{item_type}]"
    elif schema_type == "object":
        additional = schema.get("additionalProperties")
        if additional:
            value_type = openapi_type_to_python(additional, schemas)
            return f"Dict[str, {value_type}]"
        # Check if inline properties match an existing named schema
        inline_props = schema.get("properties")
        if inline_props:
            inline_keys = sorted(inline_props.keys())
            for schema_name, schema_def in schemas.items():
                defined_keys = sorted(schema_def.get("properties", {}).keys())
                if defined_keys and inline_keys == defined_keys:
                    return to_pascal_case(schema_name)
        return "Dict[str, Any]"
    else:
        return "Any"


def extract_request_body_type(
    request_body: dict[str, Any] | None, schemas: dict[str, Any]
) -> tuple[str | None, bool]:
    """Extract request body type and whether it's multipart."""
    if not request_body:
        return None, False

    content = request_body.get("content", {})

    # Check for multipart
    if "multipart/form-data" in content:
        return "dict[str, Any]", True

    # Check for JSON
    if "application/json" in content:
        schema = content["application/json"].get("schema", {})
        return openapi_type_to_python(schema, schemas), False

    return None, False


def extract_response_type(
    responses: dict[str, Any], schemas: dict[str, Any]
) -> str | None:
    """Extract successful response type."""
    for code in ["200", "201", "202", "203"]:
        if code not in responses:
            continue
        response = responses[code]
        content = response.get("content", {})
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            return openapi_type_to_python(schema, schemas)
    return None


def parse_endpoints(schema: dict[str, Any]) -> list[Endpoint]:
    """Parse all endpoints from OpenAPI schema."""
    endpoints = []
    paths = schema.get("paths", {})
    schemas = schema.get("components", {}).get("schemas", {})

    for path, methods in paths.items():
        for method, spec in methods.items():
            if method in ("parameters", "servers", "summary", "description"):
                continue

            operation_id = spec.get("operationId", f"{method}_{path}")

            parameters = []
            for param in spec.get("parameters", []):
                param_schema = param.get("schema", {})
                param_type = openapi_type_to_python(param_schema, schemas)
                parameters.append(
                    Parameter(
                        name=param["name"],
                        location=param.get("in", "query"),
                        required=param.get("required", False),
                        python_name=sanitize_python_name(param["name"]),
                        param_type=param_type,
                        description=param.get("description"),
                    )
                )

            request_body = spec.get("requestBody")
            body_type, is_multipart = extract_request_body_type(request_body, schemas)

            response_type = extract_response_type(spec.get("responses", {}), schemas)

            endpoints.append(
                Endpoint(
                    path=path,
                    method=method.upper(),
                    operation_id=operation_id,
                    summary=spec.get("summary"),
                    description=spec.get("description"),
                    deprecated=spec.get("deprecated", False),
                    parameters=parameters,
                    request_body_required=request_body.get("required", False)
                    if request_body
                    else False,
                    request_body_type=body_type,
                    response_type=response_type,
                    is_multipart=is_multipart,
                )
            )

    return endpoints


def group_by_resource(endpoints: list[Endpoint]) -> dict[str, Resource]:
    """Group endpoints by their resource (first non-parameter path segment after version)."""
    resources: dict[str, Resource] = {}

    for endpoint in endpoints:
        # Extract resource name from path: /v2/folders/{id} -> folders
        # Skip path parameters (things in braces like {folder_token})
        parts = endpoint.path.strip("/").split("/")

        # Find the first non-parameter segment after 'v2'
        resource_name = "root"
        for i, part in enumerate(parts):
            # Skip version prefix
            if part in ("v1", "v2", "v3", "api"):
                continue
            # Skip path parameters
            if part.startswith("{") and part.endswith("}"):
                continue
            resource_name = part
            break

        if resource_name not in resources:
            resources[resource_name] = Resource(name=resource_name)
        resources[resource_name].endpoints.append(endpoint)

    return resources


def generate_method_name(endpoint: Endpoint, resource_name: str) -> str:
    """Generate a method name from operation ID, stripping redundant resource names."""
    op_id = endpoint.operation_id
    resource_pascal = to_pascal_case(resource_name)
    resource_singular = resource_pascal[:-1] if resource_pascal.endswith("s") else resource_pascal

    for prefix in ["get", "create", "update", "delete", "list", "add", "remove",
                    "download", "regenerate", "send"]:
        if op_id.lower().startswith(prefix):
            remainder = op_id[len(prefix):]

            # Exact plural match = list operation (e.g. getCostReports -> list)
            if resource_pascal.endswith("s") and remainder == resource_pascal:
                return "list"

            # Strip resource name: try plural first to avoid stray 's'
            if remainder.startswith(resource_pascal):
                remainder = remainder[len(resource_pascal):]
            elif remainder.startswith(resource_singular):
                remainder = remainder[len(resource_singular):]
            elif remainder.endswith(resource_pascal):
                remainder = remainder[:-len(resource_pascal)]
            elif remainder.endswith(resource_singular):
                remainder = remainder[:-len(resource_singular)]

            if not remainder:
                return prefix
            return to_snake_case(prefix + remainder)

    return to_snake_case(op_id)


def _extract_inner_type(type_hint: str, generic_prefix: str) -> str | None:
    """Extract inner type from simple generic forms like Prefix[Inner]."""
    if not type_hint.startswith(generic_prefix) or not type_hint.endswith("]"):
        return None
    return type_hint[len(generic_prefix):-1].strip()


def _extract_dict_value_type(type_hint: str) -> str | None:
    """Extract value type from Dict[str, ValueType]."""
    if not type_hint.startswith("Dict[") or not type_hint.endswith("]"):
        return None
    inner = type_hint[len("Dict["):-1].strip()
    key_and_value = inner.split(",", 1)
    if len(key_and_value) != 2:
        return None
    key_type = key_and_value[0].strip()
    value_type = key_and_value[1].strip()
    if key_type not in {"str", "Optional[str]"}:
        return None
    return value_type


def _is_model_type(type_hint: str) -> bool:
    """Return True for generated Pydantic model type names."""
    return bool(re.match(r"^[A-Z][A-Za-z0-9_]*$", type_hint))


def _append_response_mapping(lines: list[str], return_type: str, data_var: str) -> None:
    """Append generated code that coerces dict payloads into typed models."""
    type_hint = return_type.strip()

    optional_inner = _extract_inner_type(type_hint, "Optional[")
    if optional_inner:
        type_hint = optional_inner

    list_inner = _extract_inner_type(type_hint, "List[")
    if list_inner and _is_model_type(list_inner):
        lines.extend(
            [
                f"        if isinstance({data_var}, list):",
                f"            return [{list_inner}.model_validate(item) if isinstance(item, dict) else item for item in {data_var}]",
            ]
        )
        return

    dict_inner = _extract_dict_value_type(type_hint)
    if dict_inner and _is_model_type(dict_inner):
        lines.extend(
            [
                f"        if isinstance({data_var}, dict):",
                f"            return {{k: {dict_inner}.model_validate(v) if isinstance(v, dict) else v for k, v in {data_var}.items()}}",
            ]
        )
        return

    if _is_model_type(type_hint):
        lines.extend(
            [
                f"        if isinstance({data_var}, dict):",
                f"            return {type_hint}.model_validate({data_var})",
            ]
        )


def generate_pydantic_models(schema: dict[str, Any]) -> str:
    """Generate Pydantic models from OpenAPI schemas."""
    schemas = schema.get("components", {}).get("schemas", {})
    lines = [
        '"""Auto-generated Pydantic models from OpenAPI schema."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, Optional, List, Dict",
        "",
        "from pydantic import BaseModel, Field",
        "",
        "",
    ]

    for name, spec in schemas.items():
        class_name = to_pascal_case(name)
        description = spec.get("description", "")

        lines.append(f"class {class_name}(BaseModel):")
        if description:
            lines.append(f'    """{description}"""')
            lines.append("")

        properties = spec.get("properties", {})
        required = set(spec.get("required", []))

        if not properties:
            lines.append("    pass")
            lines.append("")
            lines.append("")
            continue

        for prop_name, prop_spec in properties.items():
            python_name = to_snake_case(prop_name)

            # Avoid shadowing BaseModel attributes
            needs_alias = python_name != prop_name
            if python_name in RESERVED_FIELD_NAMES:
                python_name = python_name + "_"
                needs_alias = True

            prop_type = openapi_type_to_python(prop_spec, schemas)

            # Handle nullable
            if prop_spec.get("x-nullable") or prop_spec.get("nullable"):
                if not prop_type.startswith("Optional["):
                    prop_type = f"Optional[{prop_type}]"

            # Handle optionals
            is_required = prop_name in required
            has_default = "default" in prop_spec

            if not is_required or has_default:
                if not prop_type.startswith("Optional["):
                    prop_type = f"Optional[{prop_type}]"

            # Build field definition
            field_args = []
            if needs_alias:
                field_args.append(f'alias="{prop_name}"')
            if not is_required or has_default:
                default_val = prop_spec.get("default", None)
                if default_val is None:
                    field_args.append("default=None")
                elif isinstance(default_val, str):
                    field_args.append(f'default="{default_val}"')
                else:
                    field_args.append(f"default={default_val}")
            if prop_spec.get("description"):
                desc = prop_spec["description"]
                # Escape quotes and newlines
                desc = desc.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").replace("\r", "")
                field_args.append(f'description="{desc}"')

            if field_args:
                lines.append(f"    {python_name}: {prop_type} = Field({', '.join(field_args)})")
            else:
                lines.append(f"    {python_name}: {prop_type}")

        lines.append("")
        lines.append("")

    return "\n".join(lines)


def generate_sync_client(resources: dict[str, Resource]) -> str:
    """Generate synchronous client code."""
    lines = [
        '"""Auto-generated synchronous client for Vantage API."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, Optional, Dict, List",
        "from urllib.parse import quote",
        "",
        "import httpx",
        "",
        "from .._base import (",
        "    VantageAPIError,",
        "    DEFAULT_BASE_URL,",
        "    build_query_string,",
        "    is_multipart_route,",
        ")",
        "from .._types import *  # noqa: F401, F403",
        "",
        "",
        "class SyncClient:",
        '    """Synchronous HTTP client for Vantage API."""',
        "",
        "    def __init__(",
        "        self,",
        "        bearer_token: str,",
        "        *,",
        "        base_url: str = DEFAULT_BASE_URL,",
        "    ) -> None:",
        "        self._bearer_token = bearer_token",
        "        self._base_url = base_url.rstrip('/')",
        "        self._http = httpx.Client(",
        '            headers={"Authorization": f"Bearer {bearer_token}"},',
        "            timeout=30.0,",
        "        )",
        "",
        "        # Initialize resource APIs",
    ]

    # Add resource initializers
    for resource_name in sorted(resources.keys()):
        class_name = to_pascal_case(resource_name) + "Api"
        attr_name = to_snake_case(resource_name)
        lines.append(f"        self.{attr_name} = {class_name}(self)")

    lines.extend(
        [
            "",
            "    def close(self) -> None:",
            '        """Close the HTTP client."""',
            "        self._http.close()",
            "",
            "    def __enter__(self) -> SyncClient:",
            "        return self",
            "",
            "    def __exit__(self, *args: Any) -> None:",
            "        self.close()",
            "",
            "    def request(",
            "        self,",
            "        method: str,",
            "        path: str,",
            "        *,",
            "        params: Optional[Dict[str, Any]] = None,",
            "        body: Optional[Dict[str, Any]] = None,",
            "    ) -> Any:",
            '        """Make a raw API request."""',
            "        url = self._base_url + path",
            "",
            "        if method.upper() == 'GET' and params:",
            "            url += build_query_string(params)",
            "            params = None",
            "",
            "        if is_multipart_route(path, method):",
            "            response = self._http.request(",
            "                method,",
            "                url,",
            "                data=body,",
            "            )",
            "        else:",
            "            response = self._http.request(",
            "                method,",
            "                url,",
            "                params=params,",
            "                json=body,",
            "            )",
            "",
            "        if not response.is_success:",
            "            raise VantageAPIError(",
            "                status=response.status_code,",
            "                status_text=response.reason_phrase,",
            "                body=response.text,",
            "            )",
            "",
            "        try:",
            "            data = response.json()",
            "        except Exception:",
            "            data = None",
            "",
            "        return data",
            "",
            "",
        ]
    )

    # Generate resource API classes
    for resource_name, resource in sorted(resources.items()):
        class_name = to_pascal_case(resource_name) + "Api"
        lines.append(f"class {class_name}:")
        lines.append(f'    """API methods for {resource_name} resource."""')
        lines.append("")
        lines.append("    def __init__(self, client: SyncClient) -> None:")
        lines.append("        self._client = client")
        lines.append("")

        for endpoint in resource.endpoints:
            method_name = generate_method_name(endpoint, resource_name)
            lines.extend(generate_sync_method(endpoint, method_name))
            lines.append("")

        lines.append("")

    return "\n".join(lines)


def generate_sync_method(endpoint: Endpoint, method_name: str) -> list[str]:
    """Generate a synchronous method for an endpoint."""
    lines = []

    # Build parameter list
    params = []
    path_params = []
    query_params = []

    for param in endpoint.parameters:
        if param.location == "path":
            path_params.append(param)
            type_hint = param.param_type
            params.append(f"{param.python_name}: {type_hint}")
        elif param.location == "query":
            query_params.append(param)

    # Add request body if needed
    if endpoint.request_body_type:
        if endpoint.request_body_required:
            params.append(f"body: {endpoint.request_body_type}")
        else:
            params.append(f"body: Optional[{endpoint.request_body_type}] = None")

    # Add query params as kwargs
    if query_params:
        params.append("*")
        for qp in query_params:
            if qp.required:
                params.append(f"{qp.python_name}: {qp.param_type}")
            else:
                params.append(f"{qp.python_name}: Optional[{qp.param_type}] = None")

    # Build docstring
    doc_lines = []
    summary = sanitize_docstring(endpoint.summary)
    description = sanitize_docstring(endpoint.description)
    if summary:
        doc_lines.append(summary)
    if description and description != summary:
        if doc_lines:
            doc_lines.append("")
        doc_lines.append(description)
    if endpoint.deprecated:
        if doc_lines:
            doc_lines.append("")
        doc_lines.append(".. deprecated::")

    # Method signature
    param_str = ", ".join(["self"] + params) if params else "self"
    return_type = endpoint.response_type or "Any"
    lines.append(f"    def {method_name}({param_str}) -> {return_type}:")

    # Docstring
    if doc_lines:
        if len(doc_lines) == 1:
            lines.append(f'        """{doc_lines[0]}"""')
        else:
            lines.append('        """')
            for dl in doc_lines:
                lines.append(f"        {dl}")
            lines.append('        """')

    # Build path with parameters (URL-encode each path arg)
    path = endpoint.path
    for pp in path_params:
        path = path.replace(f"{{{pp.name}}}", f"{{quote(str({pp.python_name}), safe='')}}")

    if path_params:
        lines.append(f'        path = f"{path}"')
    else:
        lines.append(f'        path = "{path}"')

    # Build query params dict
    if query_params:
        lines.append("        params = {")
        for qp in query_params:
            lines.append(f'            "{qp.name}": {qp.python_name},')
        lines.append("        }")
    else:
        lines.append("        params = None")

    # Build body
    if endpoint.request_body_type:
        lines.append(
            "        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body"
        )
    else:
        lines.append("        body_data = None")

    # Make request and coerce response payload into typed models where possible
    lines.append(
        f'        data = self._client.request("{endpoint.method}", path, params=params, body=body_data)'
    )
    _append_response_mapping(lines, return_type, "data")
    lines.append("        return data")

    return lines


def generate_async_client(resources: dict[str, Resource]) -> str:
    """Generate asynchronous client code."""
    lines = [
        '"""Auto-generated asynchronous client for Vantage API."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, Optional, Dict, List",
        "from urllib.parse import quote",
        "",
        "import httpx",
        "",
        "from .._base import (",
        "    VantageAPIError,",
        "    DEFAULT_BASE_URL,",
        "    build_query_string,",
        "    is_multipart_route,",
        ")",
        "from .._types import *  # noqa: F401, F403",
        "",
        "",
        "class AsyncClient:",
        '    """Asynchronous HTTP client for Vantage API."""',
        "",
        "    def __init__(",
        "        self,",
        "        bearer_token: str,",
        "        *,",
        "        base_url: str = DEFAULT_BASE_URL,",
        "    ) -> None:",
        "        self._bearer_token = bearer_token",
        "        self._base_url = base_url.rstrip('/')",
        "        self._http = httpx.AsyncClient(",
        '            headers={"Authorization": f"Bearer {bearer_token}"},',
        "            timeout=30.0,",
        "        )",
        "",
        "        # Initialize resource APIs",
    ]

    # Add resource initializers
    for resource_name in sorted(resources.keys()):
        class_name = to_pascal_case(resource_name) + "AsyncApi"
        attr_name = to_snake_case(resource_name)
        lines.append(f"        self.{attr_name} = {class_name}(self)")

    lines.extend(
        [
            "",
            "    async def close(self) -> None:",
            '        """Close the HTTP client."""',
            "        await self._http.aclose()",
            "",
            "    async def __aenter__(self) -> AsyncClient:",
            "        return self",
            "",
            "    async def __aexit__(self, *args: Any) -> None:",
            "        await self.close()",
            "",
            "    async def request(",
            "        self,",
            "        method: str,",
            "        path: str,",
            "        *,",
            "        params: Optional[Dict[str, Any]] = None,",
            "        body: Optional[Dict[str, Any]] = None,",
            "    ) -> Any:",
            '        """Make a raw API request."""',
            "        url = self._base_url + path",
            "",
            "        if method.upper() == 'GET' and params:",
            "            url += build_query_string(params)",
            "            params = None",
            "",
            "        if is_multipart_route(path, method):",
            "            response = await self._http.request(",
            "                method,",
            "                url,",
            "                data=body,",
            "            )",
            "        else:",
            "            response = await self._http.request(",
            "                method,",
            "                url,",
            "                params=params,",
            "                json=body,",
            "            )",
            "",
            "        if not response.is_success:",
            "            raise VantageAPIError(",
            "                status=response.status_code,",
            "                status_text=response.reason_phrase,",
            "                body=response.text,",
            "            )",
            "",
            "        try:",
            "            data = response.json()",
            "        except Exception:",
            "            data = None",
            "",
            "        return data",
            "",
            "",
        ]
    )

    # Generate resource API classes
    for resource_name, resource in sorted(resources.items()):
        class_name = to_pascal_case(resource_name) + "AsyncApi"
        lines.append(f"class {class_name}:")
        lines.append(f'    """Async API methods for {resource_name} resource."""')
        lines.append("")
        lines.append("    def __init__(self, client: AsyncClient) -> None:")
        lines.append("        self._client = client")
        lines.append("")

        for endpoint in resource.endpoints:
            method_name = generate_method_name(endpoint, resource_name)
            lines.extend(generate_async_method(endpoint, method_name))
            lines.append("")

        lines.append("")

    return "\n".join(lines)


def generate_async_method(endpoint: Endpoint, method_name: str) -> list[str]:
    """Generate an asynchronous method for an endpoint."""
    lines = []

    # Build parameter list
    params = []
    path_params = []
    query_params = []

    for param in endpoint.parameters:
        if param.location == "path":
            path_params.append(param)
            type_hint = param.param_type
            params.append(f"{param.python_name}: {type_hint}")
        elif param.location == "query":
            query_params.append(param)

    # Add request body if needed
    if endpoint.request_body_type:
        if endpoint.request_body_required:
            params.append(f"body: {endpoint.request_body_type}")
        else:
            params.append(f"body: Optional[{endpoint.request_body_type}] = None")

    # Add query params as kwargs
    if query_params:
        params.append("*")
        for qp in query_params:
            if qp.required:
                params.append(f"{qp.python_name}: {qp.param_type}")
            else:
                params.append(f"{qp.python_name}: Optional[{qp.param_type}] = None")

    # Build docstring
    doc_lines = []
    summary = sanitize_docstring(endpoint.summary)
    description = sanitize_docstring(endpoint.description)
    if summary:
        doc_lines.append(summary)
    if description and description != summary:
        if doc_lines:
            doc_lines.append("")
        doc_lines.append(description)
    if endpoint.deprecated:
        if doc_lines:
            doc_lines.append("")
        doc_lines.append(".. deprecated::")

    # Method signature
    param_str = ", ".join(["self"] + params) if params else "self"
    return_type = endpoint.response_type or "Any"
    lines.append(f"    async def {method_name}({param_str}) -> {return_type}:")

    # Docstring
    if doc_lines:
        if len(doc_lines) == 1:
            lines.append(f'        """{doc_lines[0]}"""')
        else:
            lines.append('        """')
            for dl in doc_lines:
                lines.append(f"        {dl}")
            lines.append('        """')

    # Build path with parameters (URL-encode each path arg)
    path = endpoint.path
    for pp in path_params:
        path = path.replace(f"{{{pp.name}}}", f"{{quote(str({pp.python_name}), safe='')}}")

    if path_params:
        lines.append(f'        path = f"{path}"')
    else:
        lines.append(f'        path = "{path}"')

    # Build query params dict
    if query_params:
        lines.append("        params = {")
        for qp in query_params:
            lines.append(f'            "{qp.name}": {qp.python_name},')
        lines.append("        }")
    else:
        lines.append("        params = None")

    # Build body
    if endpoint.request_body_type:
        lines.append(
            "        body_data = body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body"
        )
    else:
        lines.append("        body_data = None")

    # Make request and coerce response payload into typed models where possible
    lines.append(
        f'        data = await self._client.request("{endpoint.method}", path, params=params, body=body_data)'
    )
    _append_response_mapping(lines, return_type, "data")
    lines.append("        return data")

    return lines


def fetch_openapi_schema() -> dict[str, Any]:
    """Fetch the OpenAPI schema from the Vantage API."""
    print(f"Fetching OpenAPI schema from {OPENAPI_URL}...")

    request = urllib.request.Request(
        OPENAPI_URL,
        headers={"Accept": "application/json", "User-Agent": "vantage-python-sdk-generator"},
    )

    with urllib.request.urlopen(request) as response:
        if response.status != 200:
            raise RuntimeError(f"Failed to fetch schema: {response.status}")
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    """Main entry point for code generation."""
    # Fetch schema
    schema = fetch_openapi_schema()

    # Preprocess inline models before any type resolution
    print("Preprocessing inline models...")
    schemas = schema.get("components", {}).get("schemas", {})
    preprocess_inline_models(schemas)

    # Parse endpoints
    print("Parsing endpoints...")
    endpoints = parse_endpoints(schema)
    print(f"Found {len(endpoints)} endpoints")

    # Group by resource
    resources = group_by_resource(endpoints)
    print(f"Found {len(resources)} resources: {', '.join(sorted(resources.keys()))}")

    # Ensure output directories exist
    sync_dir = OUTPUT_DIR / "_sync"
    async_dir = OUTPUT_DIR / "_async"
    sync_dir.mkdir(parents=True, exist_ok=True)
    async_dir.mkdir(parents=True, exist_ok=True)

    # Generate types
    print("Generating Pydantic models...")
    types_code = generate_pydantic_models(schema)
    (OUTPUT_DIR / "_types.py").write_text(types_code)

    # Generate sync client
    print("Generating sync client...")
    sync_code = generate_sync_client(resources)
    (sync_dir / "client.py").write_text(sync_code)
    (sync_dir / "__init__.py").write_text(
        '"""Synchronous Vantage API client."""\n\nfrom .client import SyncClient\n\n__all__ = ["SyncClient"]\n'
    )

    # Generate async client
    print("Generating async client...")
    async_code = generate_async_client(resources)
    (async_dir / "client.py").write_text(async_code)
    (async_dir / "__init__.py").write_text(
        '"""Asynchronous Vantage API client."""\n\nfrom .client import AsyncClient\n\n__all__ = ["AsyncClient"]\n'
    )

    print("Code generation complete!")


if __name__ == "__main__":
    main()
