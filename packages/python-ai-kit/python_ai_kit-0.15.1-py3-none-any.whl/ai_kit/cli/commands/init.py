from pathlib import Path
import logging
from rich.console import Console
from rich.prompt import Confirm
from ai_kit.utils.fs import package_root
from ai_kit.cli.templating import handle_cursorrules, handle_env_example
from ai_kit.shared_console import shared_console

def handle_global_env(source: Path) -> None:
    """Handle global ~/.ai-kit.env file creation.
    
    Creates or updates the global ~/.ai-kit.env file in the user's home directory.
    
    Args:
        source (Path): Source path of the .env.example file
    """
    global_env = Path.home() / '.ai-kit.env'
    
    try:
        # Always create/update the global config
        global_env.write_text(source.read_text())
        shared_console.print(f"[green]✓ {'Updated' if global_env.exists() else 'Created'} global config at {global_env}[/green]")
    except Exception as e:
        shared_console.print(f"[red]Error: Could not create global config file: {e}[/red]")

def init_command(log_level: str):
    """Initialize AI Kit with cursor rules and logging setup.
    
    Args:
        log_level: The logging level to set (e.g. INFO, DEBUG, etc.)
    """
    # Setup logging
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.upper())
    shared_console.print(f"[green]✓ Set logging level to {log_level}[/green]")

    # Handle cursor rules setup
    pkg_root = package_root()
    cursorrules_source = pkg_root / "system_prompts" / "cursorrules.md"  # This is just a reference point
    
    update_cursorrules = Confirm.ask(
        "[bold yellow]Would you like to create/update cursor rules with default AI Kit rules?[/bold yellow]",
        default=True
    )
    
    if update_cursorrules:
        try:
            handle_cursorrules(cursorrules_source, Path(".cursor/rules"))
        except Exception as e:
            shared_console.print(f"[red]Error: Could not update cursor rules: {e}[/red]")
            return

    # Handle .env.example file copy
    env_example_source = pkg_root / ".env.example"
    env_example_dest = Path(".env.example")
    
    # Always create/update the global ~/.ai-kit.env file
    handle_global_env(env_example_source)
    
    # Handle local .env.example file
    copy_env_example = Confirm.ask(
        "[bold yellow]Would you like to copy the .env.example file to your workspace?[/bold yellow]",
        default=True
    )
    
    if copy_env_example:
        handle_env_example(env_example_source, env_example_dest)

    shared_console.print("\n[bold green]✨ AI Kit initialization complete![/bold green]")
    shared_console.print("You can now use AI Kit commands with the configured settings.")
