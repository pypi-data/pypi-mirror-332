"""Integration tests for MCP Registry."""

import pytest

from mcp_registry import (
    MCPAggregator,
    MCPServerSettings,
    ServerRegistry,
    run_registry_server,
)


@pytest.fixture
def memory_server_config():
    """Create a memory server configuration."""
    return {
        "memory": MCPServerSettings(
            transport="stdio",
            command="npx",
            args=["-y", "@modelcontextprotocol/server-memory"],
            description="Memory server",
        )
    }


@pytest.fixture
def registry(memory_server_config):
    """Create a registry with the memory server."""
    return ServerRegistry(memory_server_config)


@pytest.fixture
def aggregator(registry):
    """Create an aggregator with the memory server."""
    return MCPAggregator(registry)


async def test_memory_server_integration(aggregator):
    """Test integration with memory server."""
    # List tools
    result = await aggregator.list_tools()
    assert result.tools is not None
    assert len(result.tools) > 0

    # Set a value
    result = await aggregator.call_tool("memory-set", {"key": "test", "value": "Hello, World!"})
    assert not result.isError

    # Get the value back
    result = await aggregator.call_tool("memory-get", {"key": "test"})
    assert not result.isError
    assert result.result == "Hello, World!"


async def test_registry_server_integration(registry):
    """Test registry server with memory server."""
    try:
        await run_registry_server(registry)
    except Exception as e:
        pytest.fail(f"Registry server failed to run: {e}")
