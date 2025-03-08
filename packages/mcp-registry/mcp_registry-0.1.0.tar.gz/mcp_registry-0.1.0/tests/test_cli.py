"""Tests for the CLI interface."""

import json
import os

import pytest
from click.testing import CliRunner

from mcp_registry.cli import cli


@pytest.fixture
def runner():
    """Create a CLI runner."""
    return CliRunner()


@pytest.fixture
def temp_config_path(tmp_path, monkeypatch):
    """Create a temporary config file path."""
    config_path = tmp_path / "config.json"
    # Patch the CONFIG_FILE path to use our temporary path
    monkeypatch.setattr("mcp_registry.cli.CONFIG_FILE", config_path)
    return config_path


def test_init_creates_config(runner, temp_config_path):
    """Test that init creates a config file."""
    result = runner.invoke(cli, ["init"])
    assert result.exit_code == 0
    assert "Initialized configuration" in result.output
    assert temp_config_path.exists()

    with open(temp_config_path) as f:
        config = json.load(f)
    assert "servers" in config
    assert "mcpServers" in config


def test_add_stdio_server(runner, temp_config_path):
    """Test adding a stdio server."""
    # First initialize the config
    runner.invoke(cli, ["init"])

    # Then add a server
    result = runner.invoke(
        cli, ["add", "test-server", "python", "-m", "mcp.contrib.file", "--description", "Test file server"]
    )

    assert result.exit_code == 0
    assert "Added server 'test-server'" in result.output

    # Verify the config was updated
    with open(temp_config_path) as f:
        config = json.load(f)

    assert "test-server" in config["servers"]
    assert config["servers"]["test-server"]["transport"] == "stdio"
    shell = os.environ.get("SHELL", "/bin/sh")
    assert config["servers"]["test-server"]["command"] == shell
    assert "python -m mcp.contrib.file" in " ".join(config["servers"]["test-server"]["args"])
    assert config["servers"]["test-server"]["description"] == "Test file server"


def test_add_sse_server(runner, temp_config_path):
    """Test adding an SSE server."""
    # First initialize the config
    runner.invoke(cli, ["init"])

    # Then add a server
    result = runner.invoke(
        cli, ["add", "remote-server", "dummy", "--url", "http://localhost:8000/sse", "--description", "Remote server"]
    )

    assert result.exit_code == 0
    assert "Added server 'remote-server'" in result.output

    # Verify the config was updated
    with open(temp_config_path) as f:
        config = json.load(f)

    assert "remote-server" in config["servers"]
    assert config["servers"]["remote-server"]["transport"] == "sse"
    assert config["servers"]["remote-server"]["url"] == "http://localhost:8000/sse"
    assert config["servers"]["remote-server"]["description"] == "Remote server"


def test_remove_server(runner, temp_config_path):
    """Test removing a server."""
    # First initialize the config
    runner.invoke(cli, ["init"])

    # Add a server
    runner.invoke(cli, ["add", "test-server", "python", "-m", "mcp.contrib.file"])

    # Then remove it
    result = runner.invoke(cli, ["remove", "test-server"])

    assert result.exit_code == 0
    assert "Removed server 'test-server'" in result.output

    # Verify the server was removed
    with open(temp_config_path) as f:
        config = json.load(f)

    assert "test-server" not in config["servers"]


def test_list_servers(runner, temp_config_path):
    """Test listing servers."""
    # First initialize the config
    runner.invoke(cli, ["init"])

    # Add a server
    runner.invoke(cli, ["add", "test-server", "python", "-m", "mcp.contrib.file"])

    # List servers
    result = runner.invoke(cli, ["list"])

    assert result.exit_code == 0
    assert "test-server" in result.output
    assert "stdio" in result.output
    assert "python -m mcp.contrib.file" in result.output


def test_list_empty(runner, temp_config_path):
    """Test listing servers when none are registered."""
    # First initialize the config
    runner.invoke(cli, ["init"])

    # List servers
    result = runner.invoke(cli, ["list"])

    assert result.exit_code == 0
    assert "No servers registered" in result.output
