"""
Utility functions for mcp_openapi_proxy, including logging setup,
OpenAPI fetching, name normalization, whitelist filtering, auth handling,
and response type detection.
"""

import os
import sys
import logging
import requests
import re
import json
import yaml
from dotenv import load_dotenv
from mcp import types
from typing import Tuple, Union, Any

# Load environment variables from .env if present
load_dotenv()

OPENAPI_SPEC_URL = os.getenv("OPENAPI_SPEC_URL")

def setup_logging(debug: bool = False) -> logging.Logger:
    """
    Configures logging for the application, directing all output to stderr.

    Args:
        debug (bool): If True, sets log level to DEBUG; otherwise, INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.propagate = False

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    if debug:
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)
        logger.debug("Logging initialized, all output to stderr")
    else:
        logger.addHandler(logging.NullHandler())
    return logger

DEBUG = os.getenv("DEBUG", "").lower() in ("true", "1", "yes")
logger = setup_logging(debug=DEBUG)

logger.debug(f"OpenAPI Spec URL: {OPENAPI_SPEC_URL}")
logger.debug("utils.py initialized")

def redact_api_key(key: str) -> str:
    """Redacts an API key for secure logging."""
    if not key or len(key) <= 4:
        return "<not set>"
    return f"{key[:2]}{'*' * (len(key) - 4)}{key[-2:]}"

def normalize_tool_name(name: str) -> str:
    """
    Normalizes tool names into a clean function name without parameters.
    For example, 'GET /sessions/{sessionId}/messages/{messageUUID}' becomes
    'get_sessions_messages'.

    Args:
        name (str): Raw method and path, e.g., 'GET /sessions/{sessionId}/messages/{messageUUID}'.

    Returns:
        str: Normalized tool name without parameters.
    """
    logger = logging.getLogger(__name__)
    if not name or not isinstance(name, str):
        logger.warning(f"Invalid tool name input: {name}. Defaulting to 'unknown_tool'.")
        return "unknown_tool"

    parts = name.strip().split(" ", 1)
    if len(parts) != 2:
        logger.warning(f"Malformed tool name '{name}', expected 'METHOD /path'. Defaulting to 'unknown_tool'.")
        return "unknown_tool"

    method, path = parts
    method = method.lower()

    path_parts = [p for p in path.split("/") if p and p not in ("api", "v2")]
    if not path_parts:
        logger.warning(f"No valid path segments in '{path}'. Using '{method}_unknown'.")
        return f"{method}_unknown"

    func_name = method
    for part in path_parts:
        if "{" in part and "}" in part:
            continue  # Skip params, they'll go in inputSchema
        else:
            func_name += f"_{part}"

    func_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", func_name)
    func_name = re.sub(r"_+", "_", func_name).strip("_")
    if len(func_name) > 64:
        func_name = func_name[:64]

    logger.debug(f"Normalized tool name from '{name}' to '{func_name}'")
    return func_name or "unknown_tool"

def get_tool_prefix() -> str:
    """Retrieves tool name prefix from environment, ensuring it ends with an underscore."""
    prefix = os.getenv("TOOL_NAME_PREFIX", "")
    if prefix and not prefix.endswith("_"):
        prefix += "_"
    return prefix

def is_tool_whitelisted(endpoint: str) -> bool:
    """
    Checks if an endpoint matches any partial path in TOOL_WHITELIST.
    Supports exact matches, prefix matches, and partial path matches with variables.

    Args:
        endpoint (str): The endpoint path from the OpenAPI spec (e.g., '/sessions/{sessionId}/messages').

    Returns:
        bool: True if the endpoint matches any whitelist item partially or exactly, False otherwise.
    """
    whitelist = os.getenv("TOOL_WHITELIST", "")
    logger.debug(f"Checking whitelist - endpoint: {endpoint}, TOOL_WHITELIST: {whitelist}")
    if not whitelist:
        logger.debug("No TOOL_WHITELIST set, allowing all endpoints.")
        return True

    whitelist_items = [item.strip() for item in whitelist.split(",") if item.strip()]
    if not whitelist_items:
        logger.debug("TOOL_WHITELIST is empty after splitting, allowing all endpoints.")
        return True

    endpoint_parts = [p for p in endpoint.split("/") if p]  # Split and filter empty

    for item in whitelist_items:
        # Exact match
        if endpoint == item:
            logger.debug(f"Exact match found for {endpoint} in whitelist")
            return True

        # Prefix match (no vars in item)
        if '{' not in item and endpoint.startswith(item):
            logger.debug(f"Prefix match found: {item} starts {endpoint}")
            return True

        # Partial path match with variables
        item_parts = [p for p in item.split("/") if p]
        if len(item_parts) <= len(endpoint_parts):
            match = True
            for i, item_part in enumerate(item_parts):
                endpoint_part = endpoint_parts[i]
                if "{" in item_part and "}" in item_part:
                    # Variable part, any value matches
                    continue
                elif item_part != endpoint_part:
                    match = False
                    break
            if match:
                logger.debug(f"Partial path match found for {endpoint} using {item}")
                return True

    logger.debug(f"No whitelist match found for {endpoint}")
    return False

def fetch_openapi_spec(spec_url: str) -> dict:
    """Fetches and parses OpenAPI specification from a URL or file, supporting JSON and YAML formats."""
    logger = logging.getLogger(__name__)
    try:
        if spec_url.startswith("file://"):
            spec_path = spec_url.replace("file://", "")
            with open(spec_path, 'r') as f:
                content = f.read()
            logger.debug(f"Read local OpenAPI spec from {spec_path}")
        else:
            response = requests.get(spec_url)
            response.raise_for_status()
            content = response.text
            logger.debug(f"Fetched OpenAPI spec from {spec_url}")

        if spec_url.endswith(('.yaml', '.yml')):
            spec = yaml.safe_load(content)
            logger.debug(f"Parsed YAML OpenAPI spec from {spec_url}")
        else:
            spec = json.loads(content)
            logger.debug(f"Parsed JSON OpenAPI spec from {spec_url}")
        return spec
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching OpenAPI spec from {spec_url}: {e}")
        return None
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        logger.error(f"Error parsing OpenAPI spec from {spec_url}: {e}")
        return None
    except FileNotFoundError as e:
        logger.error(f"Local file not found for OpenAPI spec at {spec_url}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error with OpenAPI spec from {spec_url}: {e}")
        return None

def get_auth_headers(spec: dict, api_key_env: str = "API_KEY") -> dict:
    """
    Constructs authorization headers based on spec and environment variables.

    Args:
        spec (dict): OpenAPI specification.
        api_key_env (str): Environment variable name for the API key (default: "API_KEY").

    Returns:
        dict: Headers dictionary with Authorization set appropriately.
    """
    headers = {}
    auth_token = os.getenv(api_key_env)
    if not auth_token:
        logger.debug(f"No {api_key_env} set, skipping auth headers.")
        return headers

    # Check for override first
    auth_type_override = os.getenv("API_AUTH_TYPE")
    if auth_type_override:
        headers["Authorization"] = f"{auth_type_override} {auth_token}"
        logger.debug(f"Using API_AUTH_TYPE override: Authorization: {auth_type_override} {redact_api_key(auth_token)}")
        return headers

    # Parse spec’s security definitions
    security_defs = spec.get('securityDefinitions', {})
    for name, definition in security_defs.items():
        if definition.get('type') == 'apiKey' and definition.get('in') == 'header' and definition.get('name') == 'Authorization':
            desc = definition.get('description', '')
            match = re.search(r'(\w+(?:-\w+)*)\s+<token>', desc)
            if match:
                prefix = match.group(1)  # e.g., "Api-Key"
                headers["Authorization"] = f"{prefix} {auth_token}"
                logger.debug(f"Using apiKey with prefix from spec description: Authorization: {prefix} {redact_api_key(auth_token)}")
            else:
                headers["Authorization"] = auth_token
                logger.debug(f"Using raw apiKey auth from spec: Authorization: {redact_api_key(auth_token)}")
            return headers
        elif definition.get('type') == 'oauth2':
            headers["Authorization"] = f"Bearer {auth_token}"
            logger.debug(f"Using Bearer auth from spec: Authorization: Bearer {redact_api_key(auth_token)}")
            return headers

    # Fallback if no clear auth type
    headers["Authorization"] = auth_token
    logger.warning(f"No clear auth type in spec, using raw API key: Authorization: {redact_api_key(auth_token)}")
    return headers

def map_schema_to_tools(schema: dict) -> list:
    """Maps a schema to a list of MCP tools."""
    from mcp import types
    tools = []
    classes = schema.get("classes", [])
    for entry in classes:
        cls = entry.get("class", "")
        if not cls:
            continue
        tool_name = normalize_tool_name(cls)
        prefix = os.getenv("TOOL_NAME_PREFIX", "")
        if prefix:
            if not prefix.endswith("_"):
                prefix += "_"
            tool_name = prefix + tool_name
        description = f"Tool for class {cls}: " + json.dumps(entry)
        tool = types.Tool(name=tool_name, description=description, inputSchema={"type": "object"})
        tools.append(tool)
    return tools

def detect_response_type(response_text: str) -> Tuple[types.TextContent, str]:
    """
    Detect the response type (JSON or text) and return the appropriate MCP content object.

    Args:
        response_text (str): The raw response text from the HTTP request.

    Returns:
        Tuple: (content object, log message)
    """
    logger = logging.getLogger(__name__)
    try:
        json.loads(response_text)
        content = types.TextContent(type="json", text=response_text)
        log_message = "Detected JSON response"
    except json.JSONDecodeError:
        content = types.TextContent(type="text", text=response_text)
        log_message = "Detected non-JSON response, falling back to text"
    return content, log_message
