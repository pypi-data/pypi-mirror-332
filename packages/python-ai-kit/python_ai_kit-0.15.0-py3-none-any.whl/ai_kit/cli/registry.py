import inspect
import json
from typing import Optional, Dict
from ai_kit.shared_console import shared_console
import click

class CommandRegistry:
    def __init__(self):
        self.commands = []

    def add(self, name: str, description: str, usage: str, metadata: Optional[Dict] = None, beta: bool = False):
        """Decorator to register commands with metadata."""
        def decorator(func):
            # Grab the function's signature for argument info
            sig = inspect.signature(func)

            # Build a list of parameter metadata
            parameters = []
            for param_name, param_obj in sig.parameters.items():
                # If no type annotation, default to 'Any'
                param_type = (
                    param_obj.annotation.__name__ 
                    if (param_obj.annotation != inspect._empty and hasattr(param_obj.annotation, '__name__'))
                    else "Any"
                )

                # If parameter has a default, store it; otherwise None
                default_value = (
                    param_obj.default 
                    if param_obj.default != inspect._empty 
                    else None
                )

                parameters.append({
                    "name": param_name,
                    "type": param_type,
                    "default": default_value
                })

            # Build metadata dictionary for this command
            command_info = {
                "name": name if name else func.__name__,
                "description": description or "No description provided.",
                # "docstring": func.__doc__ or "No docstring available.",
                "parameters": parameters,
                "metadata": metadata,
                "usage": usage,
                "beta": beta
            }

            # Store in our registry
            self.commands.append(command_info)

            # Return the original function so it still works
            return func
        return decorator

    @property
    def xml_prompt(self):
        """Return a string-based prompt with JSON metadata for each command."""
        xml_parts = ['<commands_configuration>']
        
        for cmd in self.commands:
            xml_parts.append('<command>')
            xml_parts.append(f'<n>{cmd["name"]}</n>')
            xml_parts.append(f'<description>{cmd["description"]}</description>')
            
            # Add beta flag if true
            if cmd.get("beta", False):
                xml_parts.append('<beta>true</beta>')
            
            # Add parameters section if there are any
            if cmd["parameters"]:
                xml_parts.append('<parameters>')
                for param in cmd["parameters"]:
                    param_info = [
                        f'<parameter>',
                        f'<n>{param["name"]}</n>',
                        f'<type>{param["type"]}</type>'
                    ]
                    if param["default"] is not None:
                        param_info.append(f'<default>{param["default"]}</default>')
                    param_info.append('</parameter>')
                    xml_parts.extend(param_info)
                xml_parts.append('</parameters>')
            
            # Add any additional metadata if present
            if cmd["metadata"]:
                for key, value in cmd["metadata"].items():
                    xml_parts.append(f'<{key}>{value}</{key}>')
            
            xml_parts.append('</command>')
        
        xml_parts.append('</commands_configuration>')
        return '\n'.join(xml_parts)
    
    @property
    def markdown_prompt(self):
        """Return a markdown-based prompt with JSON metadata for each command."""
        markdown_parts = ['# Commands Configuration\n']
        
        # Regular commands section
        markdown_parts.append('## Regular Commands\n')
        regular_commands = [cmd for cmd in self.commands if not cmd.get("beta", False)]
        
        for cmd in regular_commands:
            # Command header and description
            markdown_parts.append(f'### {cmd["name"]}')
            markdown_parts.append(f'{cmd["description"]}\n')
            
            # Parameters section
            if cmd["parameters"]:
                markdown_parts.append('#### Parameters')
                for param in cmd["parameters"]:
                    param_desc = [f'- **{param["name"]}** (`{param["type"]}`):']
                    if param["default"] is not None:
                        param_desc.append(f' Default: `{param["default"]}`')
                    markdown_parts.append(''.join(param_desc))
                markdown_parts.append('')  # Empty line after parameters
            
            # Additional metadata section
            if cmd["metadata"]:
                markdown_parts.append('#### Additional Information')
                for key, value in cmd["metadata"].items():
                    markdown_parts.append(f'- **{key}**: {value}')
                markdown_parts.append('')  # Empty line after metadata
            
            markdown_parts.append('---\n')  # Separator between commands
        
        # Beta commands section
        beta_commands = [cmd for cmd in self.commands if cmd.get("beta", False)]
        if beta_commands:
            markdown_parts.append('## Beta Commands\n')
            markdown_parts.append('> ⚠️ These commands are in beta and may change without notice.\n')
            
            for cmd in beta_commands:
                # Command header and description
                markdown_parts.append(f'### {cmd["name"]} (Beta)')
                markdown_parts.append(f'{cmd["description"]}\n')
                
                # Parameters section
                if cmd["parameters"]:
                    markdown_parts.append('#### Parameters')
                    for param in cmd["parameters"]:
                        param_desc = [f'- **{param["name"]}** (`{param["type"]}`):']
                        if param["default"] is not None:
                            param_desc.append(f' Default: `{param["default"]}`')
                        markdown_parts.append(''.join(param_desc))
                    markdown_parts.append('')  # Empty line after parameters
                
                # Additional metadata section
                if cmd["metadata"]:
                    markdown_parts.append('#### Additional Information')
                    for key, value in cmd["metadata"].items():
                        markdown_parts.append(f'- **{key}**: {value}')
                    markdown_parts.append('')  # Empty line after metadata
                
                markdown_parts.append('---\n')  # Separator between commands
        
        return '\n'.join(markdown_parts)

    def display_commands(self):
        """Display commands in a rich formatted table."""
        from rich.table import Table
        from rich.panel import Panel
        from rich.text import Text
        from rich.box import SIMPLE

        # Create a list of standard commands and beta commands
        standard_commands = [cmd for cmd in self.commands if not cmd.get("beta", False)]
        beta_commands = [cmd for cmd in self.commands if cmd.get("beta", False)]

        # Create the main table for standard commands
        table = Table(
            title="Available Commands", 
            show_header=True, 
            header_style="bold magenta",
            show_lines=True,
            border_style="bright_cyan"
        )
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")
        table.add_column("Parameters", style="yellow")
        table.add_column("Usage (aik=ai-kit) ", style="blue")
        # table.add_column("Metadata", style="blue")

        for cmd in standard_commands:
            # Format parameters
            params = []
            for p in cmd["parameters"]:
                param_text = f"{p['name']}: {p['type']}"
                if p["default"] is not None:
                    param_text += f" (default: {p['default']})"
                params.append(param_text)
            params_str = "\n".join(params)

            # Format usage
            usage_str = cmd["usage"]

            # Format metadata
            metadata_str = "\n".join(f"{k}: {v}" for k, v in (cmd["metadata"] or {}).items()) or ""

            table.add_row(
                cmd["name"],
                cmd["description"],
                params_str,
                usage_str,
                # metadata_str or ""
            )

        # Display the table
        shared_console.print(table)

        # If there are beta commands, display them in a separate table
        if beta_commands:
            beta_table = Table(
                title="Beta Commands", 
                show_header=True, 
                header_style="bold magenta",
                show_lines=True,
                border_style="bright_yellow"
            )
            beta_table.add_column("Command", style="cyan")
            beta_table.add_column("Description", style="green")
            beta_table.add_column("Parameters", style="yellow")
            beta_table.add_column("Usage (aik=ai-kit) ", style="blue")
            # beta_table.add_column("Metadata", style="blue")

            for cmd in beta_commands:
                # Format parameters
                params = []
                for p in cmd["parameters"]:
                    param_text = f"{p['name']}: {p['type']}"
                    if p["default"] is not None:
                        param_text += f" (default: {p['default']})"
                    params.append(param_text)
                params_str = "\n".join(params)

                # Format usage
                usage_str = cmd["usage"]

                # Format metadata
                metadata_str = "\n".join(f"{k}: {v}" for k, v in (cmd["metadata"] or {}).items()) or ""

                beta_table.add_row(
                    cmd["name"],
                    cmd["description"],
                    params_str,
                    usage_str,
                    # metadata_str or ""
                )

            # Display the beta table
            shared_console.print("\n")  # Add some space between tables
            shared_console.print(beta_table)

registry_instance = CommandRegistry()