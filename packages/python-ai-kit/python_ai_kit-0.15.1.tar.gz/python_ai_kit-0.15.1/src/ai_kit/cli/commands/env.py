from rich.table import Table
from rich.text import Text
from rich.markup import escape
from dotenv import load_dotenv, find_dotenv
from ai_kit.shared_console import shared_console
import os
from pathlib import Path
from ai_kit.config.client_config import ClientFactory
import subprocess
import platform
import shutil

def obscure_key(key: str) -> str:
    if not key:
        return "not set"
    return key[:6] + "..." + key[-4:]

def get_relative_path(path: Path) -> str:
    """Convert absolute path to relative path using ~ for home directory."""
    try:
        # Resolve the path to handle any symlinks
        resolved_path = path.resolve()
        home = Path.home().resolve()
        
        # Check if the path is under home directory
        try:
            relative = resolved_path.relative_to(home)
            return f"~/{relative}"
        except ValueError:
            return str(resolved_path)
    except Exception:
        return str(path)

def make_path_clickable(path: str) -> Text:
    """Make a file path clickable by converting it to a file URL using OSC 8 sequences."""
    if path == "N/A":
        return Text(path)
    
    # Convert to absolute path for existence check
    if path.startswith("~/"):
        # Expand ~ to home directory for existence check
        abs_path = str(Path.home().resolve() / path[2:])
        display_path = path  # Keep ~ in display
    else:
        abs_path = str(Path(path).resolve())
        display_path = path

    # Only make it clickable if the file exists
    if Path(abs_path).exists():
        # Use OSC 8 escape sequences for terminal hyperlinks
        link_start = "\x1b]8;;file://" + abs_path + "\x1b\\"
        link_end = "\x1b]8;;\x1b\\"
        return Text.from_ansi(f"{link_start}{display_path}{link_end}")
    return Text(display_path)

def get_env_source(var_name: str) -> tuple[str, str]:
    """Get the source of an environment variable.
    
    Returns:
        tuple: (source description, config path)
    """
    # Check local .env first (highest precedence)
    local_env = Path('.env')
    if local_env.exists():
        with open(local_env) as f:
            if any(line.startswith(f"{var_name}=") for line in f):
                return "Local", ".env"
    
    # Check global config
    global_env = Path.home() / '.ai-kit.env'
    if global_env.exists():
        with open(global_env) as f:
            if any(line.startswith(f"{var_name}=") for line in f):
                return "Global", "~/.ai-kit.env"
    
    # If set but not found in files, it's from the system
    if os.getenv(var_name):
        return "System", "N/A"
    
    return "Not Set", "N/A"

def env_command() -> None:
    """Display AI Kit environment variables information."""
    # Show global config info
    global_env = Path.home() / '.ai-kit.env'
    exists = global_env.exists()
    status = "✓" if exists else "(not created)"
    status_style = "green" if exists else "red"
    
    shared_console.print()
    shared_console.print(
        f"AI Kit env file: [{status_style}]{status}[/{status_style}] {make_path_clickable('~/.ai-kit.env')} (cmd+click to edit)"
    )
    
    # Add contextual help text
    if exists:
        shared_console.print(
            "[dim]Global config file for AI Kit API keys and settings. Local .env files will override these settings.[/dim]"
        )
    else:
        shared_console.print(
            "[yellow]Run [bold blue]ai-kit init[/bold blue] to create your global config file.[/yellow]"
        )
    shared_console.print()
    
    # Create main env table
    table = Table(
        title="🔧 Environment Variables",
        title_style="bold cyan",
        show_header=True,
        box=None,
        padding=(0, 1)
    )
    table.add_column("Variable", style="bold blue")
    table.add_column("Value", style="white")
    table.add_column("Source", style="yellow")
    
    # Add API keys section
    table.add_row(
        Text("API Keys", style="bold yellow"),
        "", ""
    )
    
    for api_key in ClientFactory.get_api_keys_and_urls():
        var_name = api_key["name"]
        value = os.getenv(var_name)
        source, _ = get_env_source(var_name)
        
        has_key = value is not None
        status_style = "green" if has_key else "red"
        status_icon = "✓" if has_key else "(not set)"
        
        table.add_row(
            f"  {var_name}",
            Text(
                f"{status_icon} {obscure_key(value) if has_key else 'not set'}", 
                style=status_style
            ),
            source
        )

    shared_console.print(table)
    shared_console.print()

def open_env_command() -> None:
    """Open the global .ai-kit.env file in an editor."""
    global_env = Path.home() / '.ai-kit.env'
    
    # Check if file exists
    if not global_env.exists():
        shared_console.print("[yellow]Global config file does not exist.[/yellow]")
        shared_console.print("Run [bold blue]ai-kit init[/bold blue] to create your global config file.")
        return
    
    try:
        if platform.system() == 'Darwin':  # macOS
            subprocess.run(['open', '-a', 'TextEdit', str(global_env)], check=True)
        elif platform.system() == 'Windows':
            subprocess.run(['notepad', str(global_env)], check=True)
        else:  # Linux and others
            # Try common text editors in order
            editors = ['gedit', 'nano', 'vim']
            for editor in editors:
                if shutil.which(editor):
                    subprocess.run([editor, str(global_env)], check=True)
                    return
            
            shared_console.print("[red]No suitable text editor found. Please install a text editor like gedit, nano, or vim.[/red]")
    except subprocess.CalledProcessError as e:
        shared_console.print(f"[red]Error opening file: {e}[/red]") 