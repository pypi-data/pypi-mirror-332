import inspect
from ai_kit.config.client_config import ClientFactory
from ai_kit.shared_console import shared_console, shared_error_console
from ai_kit.utils.logging import rich_print_stream
from docstring_parser import parse
from ai_kit.utils.fs import load_system_prompt, package_root
from typing import Dict, List, Any
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED

def function_to_json_openai(func) -> dict:
    """
    Converts a Python function into a JSON-serializable dictionary
    that describes the function's signature, including its name,
    description, and parameters.

    Args:
        func: The function to be converted.

    Returns:
        A dictionary representing the function's signature in JSON format.
    """
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )

    parameters = {}
    for param in signature.parameters.values():
        try:
            param_type = type_map.get(param.annotation, "string")
        except KeyError as e:
            raise KeyError(
                f"Unknown type annotation {param.annotation} for parameter {param.name}: {str(e)}"
            )
        parameters[param.name] = {"type": param_type}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect._empty
    ]

    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }


def function_to_json_anthropic(func) -> dict:
    """
    Converts a Python function into a JSON-serializable dictionary
    that describes the function's signature for Anthropic's tool call format.

    Args:
        func: The function to be converted.

    Returns:
        A dictionary representing the function's signature in Anthropic's tool format.
    """
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    # Map for docstring type descriptions to JSON schema types
    docstring_type_map = {
        "str": "string",
        "string": "string",
        "int": "integer",
        "integer": "integer",
        "float": "number",
        "number": "number",
        "bool": "boolean",
        "boolean": "boolean",
        "list": "array",
        "array": "array",
        "dict": "object",
        "object": "object",
        "none": "null",
        "null": "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )

    # Parse docstring to extract parameter descriptions and types
    docstring_obj = parse(func.__doc__ or "")
    param_descriptions = {}
    param_types_from_docstring = {}

    for param in docstring_obj.params:
        param_descriptions[param.arg_name] = param.description

        # Extract type from docstring if available
        if param.type_name:
            clean_type = param.type_name.lower().strip()
            param_types_from_docstring[param.arg_name] = docstring_type_map.get(
                clean_type, "string"
            )

    # Get the short description from the parsed docstring
    description = docstring_obj.short_description or ""

    properties = {}
    for param in signature.parameters.values():
        # Priority 1: Use type hint from function signature if available
        if param.annotation is not inspect._empty:
            try:
                param_type = type_map.get(param.annotation, "string")
            except KeyError as e:
                # If type hint can't be mapped, try docstring type
                param_type = param_types_from_docstring.get(param.name, "string")
        else:
            # Priority 2: Use type from docstring if available
            param_type = param_types_from_docstring.get(param.name, "string")

        # Get description from docstring if available, otherwise use default
        description_param = param_descriptions.get(
            param.name, f"Parameter {param.name}"
        )

        # Create a property entry with type and description
        properties[param.name] = {"type": param_type, "description": description_param}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect._empty
    ]

    return {
        "name": func.__name__,
        "description": description,
        "input_schema": {
            "type": "object",
            "properties": properties,
            "required": required,
        },
    }

# Helper function to safely get attribute from objects that might be Pydantic models or dicts
def safe_get(obj, attr, default=None):
    if hasattr(obj, attr):
        return getattr(obj, attr)
    elif isinstance(obj, dict):
        return obj.get(attr, default)
    return default

async def generate_augmented_research_query(prompt: str, model: str = "gemini-2.0-flash") -> str:
    """
    Generate an augmented query for a research-oriented AI agent.

    Args:
        prompt (str): The user's initial query.
        model (str, optional): The model to use for the query augmentation. Defaults to "gemini-2.0-flash".
    """

    PACKAGE_ROOT = package_root()
    QUERY_AUGMENTATION_SYSTEM_PROMPT_PATH = f"{PACKAGE_ROOT}/system_prompts/agent/query_augmentation.md"
    QUERY_AUGMENTATION_SYSTEM_PROMPT = load_system_prompt(QUERY_AUGMENTATION_SYSTEM_PROMPT_PATH)
    client = ClientFactory.get_client_by_model(model)
    response_stream = await client.chat_completion(
        messages=[
            {"role": "system", "content": QUERY_AUGMENTATION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        stream=True
    )
    final_res = await rich_print_stream(response_stream, style="blue")
    return final_res

def print_final_answer(answer: str):
    """
    Print the final answer in a rounded panel with a blue border.
    
    Args:
        answer: The text content to display
    """
    answer_panel = Panel(
        answer,
        title="Final Answer",
        border_style="blue",
        box=ROUNDED,
        padding=(1, 2)
    )
    shared_console.print("\n\n")
    shared_console.print(answer_panel)


def print_tool_counts(tool_counts: Dict[str, int]):
    """
    Print the tool usage counts in a formatted table.
    
    Args:
        tool_counts: Dictionary mapping tool names to their usage counts
    """
    table = Table(title="Tool Usage", border_style="blue", box=ROUNDED)
    table.add_column("Tool", style="yellow")
    table.add_column("Count", style="green")
    
    for tool_name, count in tool_counts.items():
        table.add_row(tool_name, str(count))
    
    shared_console.print("\n")
    shared_console.print(table)


def print_agent_config(max_iterations: int, available_tools: List[str]):
    """
    Print the agent configuration in a formatted table.
    
    Args:
        max_iterations: Maximum number of iterations the agent will run
        available_tools: List of tool names available to the agent
    """
    table = Table(title="Agent Configuration", border_style="blue", box=ROUNDED)
    table.add_column("Setting", style="yellow")
    table.add_column("Value", style="green")
    
    table.add_row("Max Iterations", str(max_iterations))
    table.add_row("Available Tools", ", ".join(available_tools))
    
    shared_console.print("\n")
    shared_console.print(table)
