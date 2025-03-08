# src/mcp_registry/cli.py
import asyncio
import json
import os
from pathlib import Path

import click

from mcp_registry.compound import MCPServerSettings, ServerRegistry, run_registry_server

# Default config location with override via environment variable
def get_default_config_path():
    """Get the default config path respecting XDG_CONFIG_HOME."""
    xdg_config_home = os.getenv("XDG_CONFIG_HOME", str(Path.home() / ".config"))
    return Path(xdg_config_home) / "mcp_registry" / "mcp_registry_config.json"

CONFIG_FILE = Path(os.getenv("MCP_REGISTRY_CONFIG", str(get_default_config_path())))

def get_config_path():
    """Get the current config path."""
    return CONFIG_FILE

def set_config_path(path):
    """Set the config path globally."""
    global CONFIG_FILE
    CONFIG_FILE = Path(path).resolve()
    return CONFIG_FILE


def load_config():
    """Load the configuration file or return an empty config if it doesn't exist."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {"servers": {}, "mcpServers": {}}


def save_config(config):
    """Save the configuration to the file, creating the directory if needed."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def find_claude_desktop_config():
    """Find the Claude Desktop config file path if it exists."""
    claude_config_path = None
    if os.name == "posix":  # Mac or Linux
        claude_config_path = Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif os.name == "nt":  # Windows
        appdata = os.getenv("APPDATA")
        if appdata:
            claude_config_path = Path(appdata) / "Claude" / "claude_desktop_config.json"

    if claude_config_path and claude_config_path.exists():
        return claude_config_path
    return None


@click.group()
def cli():
    """MCP Registry CLI tool for managing and serving MCP servers.

    Configuration file location can be set via MCP_REGISTRY_CONFIG environment variable.
    Use 'show-config-path' command to see current location.
    """
    pass


@cli.command()
@click.option("--force", is_flag=True, help="Override existing configuration if it exists")
def init(force):
    """Initialize the MCP Registry configuration.

    This command creates a new configuration file and offers to import
    settings from Claude Desktop if available.
    """
    click.echo(f"Using config file: {CONFIG_FILE}", err=True)

    if CONFIG_FILE.exists() and not force:
        if not click.confirm("Configuration file already exists. Do you want to overwrite it?", err=True):
            click.echo("Keeping existing configuration.", err=True)
            return

    # Create a new empty config
    config = {"servers": {}, "mcpServers": {}}

    # Check for Claude Desktop config
    claude_config_path = find_claude_desktop_config()
    if claude_config_path:
        if click.confirm(f"Found Claude Desktop config at {claude_config_path}. Do you want to import it?", err=True):
            try:
                with open(claude_config_path) as f:
                    claude_config = json.load(f)

                # Import servers from Claude Desktop config
                if "mcpServers" in claude_config:
                    config["mcpServers"] = claude_config["mcpServers"]

                    # Also convert to our internal format
                    for name, settings in claude_config["mcpServers"].items():
                        server_settings = {
                            "transport": "stdio",
                            "command": settings["command"],
                            "args": settings["args"],
                        }
                        if "env" in settings:
                            server_settings["env"] = settings["env"]
                        config["servers"][name] = server_settings

                    click.echo(f"Imported {len(config['mcpServers'])} servers from Claude Desktop config.", err=True)
            except Exception as e:
                click.echo(f"Error importing Claude Desktop config: {e}", err=True)

    # Save the config
    save_config(config)
    click.echo(f"Initialized configuration at {CONFIG_FILE}", err=True)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("server_name")
@click.argument("command")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
@click.option("--env", multiple=True, help="Environment variables in KEY=VALUE format")
@click.option("--description", help="Description of the server")
@click.option("--url", help="URL for sse transport (default is stdio transport)")
def add(server_name, command, args, env, description, url):
    """Add a new server to the registry.

    Example:
        mcp-registry add memory npx -y @modelcontextprotocol/server-memory
        mcp-registry add remote-sse --url http://localhost:8000/sse
    """
    # Ensure config file exists
    if not CONFIG_FILE.exists():
        click.echo("Configuration file not found. Run 'mcp-registry init' first.", err=True)
        return

    config = load_config()

    if server_name in config["servers"]:
        if not click.confirm(f"Server '{server_name}' already exists. Overwrite?", err=True):
            return

    # Process environment variables
    env_dict = {}
    if env:
        for env_var in env:
            if "=" in env_var:
                key, value = env_var.split("=", 1)
                env_dict[key] = value
            else:
                click.echo(f"Warning: Ignoring invalid environment variable format: {env_var}", err=True)

    # Debug: Show current PATH
    click.echo(f"Current PATH: {os.environ.get('PATH', '')}", err=True)

    # Always include current environment PATH and other important variables
    env_dict["PATH"] = os.environ.get("PATH", "")

    # Debug: Show shell environment
    click.echo(f"Shell: {os.environ.get('SHELL', 'unknown')}", err=True)

    # Include other important environment variables
    for var in ["NODE_PATH", "NPM_CONFIG_PREFIX", "NVM_DIR"]:
        if var in os.environ:
            env_dict[var] = os.environ[var]
            click.echo(f"Including {var}: {os.environ[var]}", err=True)

    if url:
        # SSE transport
        server_settings = {"transport": "sse", "url": url}
        if description:
            server_settings["description"] = description
        if env_dict:
            server_settings["env"] = env_dict
    else:
        # For stdio transport, try to find the full path of the command
        shell = os.environ.get("SHELL", "/bin/sh")

        # Debug: Try to find command
        click.echo(f"Using shell: {shell}", err=True)
        click.echo(f"Trying to find command '{command}'...", err=True)

        # Use the shell to find the command
        try:
            import subprocess

            full_command = subprocess.check_output([shell, "-c", f"which {command}"], text=True).strip()
            click.echo(f"Found command at: {full_command}", err=True)
        except subprocess.CalledProcessError:
            click.echo(f"Warning: Could not find '{command}' using shell, using as is", err=True)
            full_command = command

        # STDIO transport (default)
        server_settings = {
            "transport": "stdio",
            "command": shell,
            "args": ["-c", f"{full_command} " + " ".join(args)],
            "env": env_dict,  # Always include env for stdio transport
        }
        if description:
            server_settings["description"] = description

        # Store in both formats for compatibility
        config["mcpServers"][server_name] = {
            "command": shell,
            "args": ["-c", f"{full_command} " + " ".join(args)],
            "env": env_dict,
        }

    # Always store in servers format
    config["servers"][server_name] = server_settings
    save_config(config)
    click.echo(f"Added server '{server_name}' with command: {full_command if not url else url}", err=True)
    if env_dict:
        click.echo(f"Environment variables: {', '.join(f'{k}={v}' for k, v in env_dict.items())}", err=True)

    # Debug: Show final configuration
    click.echo("\nFinal server configuration:", err=True)
    click.echo(json.dumps(server_settings, indent=2), err=True)


@cli.command()
@click.argument("server_name")
def remove(server_name):
    """Remove a server from the registry."""
    # Ensure config file exists
    if not CONFIG_FILE.exists():
        click.echo("Configuration file not found. Run 'mcp-registry init' first.", err=True)
        return

    config = load_config()

    removed = False
    if server_name in config["servers"]:
        del config["servers"][server_name]
        removed = True

    if server_name in config.get("mcpServers", {}):
        del config["mcpServers"][server_name]
        removed = True

    if removed:
        save_config(config)
        click.echo(f"Removed server '{server_name}'.", err=True)
    else:
        click.echo(f"Server '{server_name}' not found.", err=True)


@cli.command(name="list")
def list_servers():
    """List all registered servers."""
    # Ensure config file exists
    click.echo(f"Using config file: {CONFIG_FILE}", err=True)

    if not CONFIG_FILE.exists():
        click.echo("Configuration file not found. Run 'mcp-registry init' first.", err=True)
        return

    config = load_config()

    if not config["servers"]:
        click.echo("No servers registered.", err=True)
        return

    click.echo("Registered servers:", err=True)
    for name, settings in sorted(config["servers"].items()):
        desc = f" - {settings.get('description')}" if settings.get("description") else ""

        if settings["transport"] == "stdio":
            cmd = f"{settings['command']} {' '.join(settings['args'])}"
            click.echo(f"  {name}: stdio ({cmd}){desc}", err=True)
        elif settings["transport"] == "sse":
            click.echo(f"  {name}: sse ({settings['url']}){desc}", err=True)
        else:
            click.echo(f"  {name}: unknown transport {settings['transport']}{desc}", err=True)


@cli.command()
@click.argument("servers", nargs=-1)
def serve(servers):
    """Serve the specified servers as a compound server.

    If no servers are specified, all registered servers will be served.

    Example:
        mcp-registry serve memory filesystem
        mcp-registry serve  # serves all registered servers
    """
    # Ensure config file exists
    if not CONFIG_FILE.exists():
        click.echo("Configuration file not found. Run 'mcp-registry init' first.", err=True)
        return

    config = load_config()

    if not config["servers"]:
        click.echo("No servers registered. Use 'add' to register servers first.", err=True)
        return

    # Create registry from config
    registry = ServerRegistry({name: MCPServerSettings(**settings) for name, settings in config["servers"].items()})

    # Determine which servers to use
    server_names = list(servers) if servers else None

    # Check if all specified servers exist
    if server_names:
        missing_servers = [s for s in server_names if s not in config["servers"]]
        if missing_servers:
            click.echo(f"Error: Servers not found: {', '.join(missing_servers)}", err=True)
            return

        click.echo(f"Serving {len(server_names)} servers: {', '.join(server_names)}", err=True)
    else:
        click.echo(f"Serving all {len(config['servers'])} registered servers", err=True)

    # Run the compound server
    asyncio.run(run_registry_server(registry, server_names))


@cli.command(name="show-config-path")
def show_config_path():
    """Show the current config file path."""
    click.echo(f"Current config file: {get_config_path()}", err=True)
    if os.getenv("MCP_REGISTRY_CONFIG"):
        click.echo("(Set via MCP_REGISTRY_CONFIG environment variable)", err=True)
    else:
        click.echo("(Using default config location)", err=True)


if __name__ == "__main__":
    cli()
