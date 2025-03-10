import sys
from rich.table import Table
from rich.text import Text
from rich import box
from ai_kit.config.client_config import ClientFactory
from ai_kit.shared_console import shared_console

def models_command():
    """Display available models grouped by provider with rich formatting."""
    try:
        # Create the main table
        table = Table(
            show_header=True,
            header_style="bold magenta",
            box=box.ROUNDED,
            title="[bold]Available AI Models[/bold]",
            title_style="bold blue",
            expand=True,
            style="cyan"
        )
        
        # Add columns
        table.add_column("Provider", style="bold cyan")
        table.add_column("Model Alias", style="yellow")
        table.add_column("Full Model ID", style="cyan")
        
        # Add rows for each provider and their models
        providers = list(ClientFactory.clients.items())
        for i, (client_name, client_info) in enumerate(providers):
            first_row = True
            if isinstance(client_info["supported_models"], dict):
                for alias, model_id in client_info["supported_models"].items():
                    if first_row:
                        table.add_row(
                            f"[bold]{client_name.upper()}[/bold]",
                            alias,
                            model_id,
                            end_section=(i < len(providers) - 1)  # Add line after provider except for last one
                        )
                        first_row = False
                    else:
                        table.add_row(
                            "",
                            alias,
                            model_id,
                        )
            else:
                # Handle special cases like perplexity's list format
                for model in client_info["supported_models"]:
                    if first_row:
                        table.add_row(
                            f"[bold]{client_name.upper()}[/bold]",
                            model,
                            model,
                            end_section=(i < len(providers) - 1)  # Add line after provider except for last one
                        )
                        first_row = False
                    else:
                        table.add_row(
                            "",
                            model,
                            model,
                        )
        
        # Print everything
        shared_console.print("\n")
        shared_console.print(table)
        shared_console.print("\n")
    except Exception as e:
        shared_console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1) 