import anthropic
import json
import copy
from typing import List, Dict, Any, Callable, Tuple, cast
from anthropic.types import Message
from anthropic._streaming import AsyncStream
from anthropic.types import (
    RawMessageStreamEvent,
    RawContentBlockStartEvent,
    RawContentBlockDeltaEvent,
    RawContentBlockStopEvent,
    RawMessageDeltaEvent,
    RawMessageStopEvent,
    InputJSONDelta,
    TextDelta,
    CitationsDelta,
)
import asyncio
from anthropic import AsyncAnthropic
from anthropic._exceptions import AnthropicError
from ai_kit.utils.fs import package_root, load_system_prompt
from pydantic import BaseModel
from ai_kit.core.agents.utils import function_to_json_anthropic
from ai_kit.shared_console import shared_console, shared_error_console
from ai_kit.core.agents.utils import print_tool_counts, print_agent_config


# Couldnt find this type so putting this here
class ThinkingDelta(BaseModel):
    type: str = "thinking_delta"
    thinking: str


# ? https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
class ThinkingConfig(BaseModel):
    type: str = "enabled"
    budget_tokens: int = 16000


PACKAGE_ROOT = package_root()
DEFAULT_SYSTEM_PROMPT_PATH = f"{PACKAGE_ROOT}/system_prompts/agent/default.md"
DEFAULT_SYSTEM_PROMPT = load_system_prompt(DEFAULT_SYSTEM_PROMPT_PATH)

EXTRA_THINKING_PROMPT = (
    "Before calling a tool, do some analysis within \<thinking>\</thinking> tags."
)

async def handle_tool_call(tool_call: Dict[str, Any], functions: List[Callable]) -> Any:
    """
    Simple function to handle a single Anthropic tool call.
    Executes the corresponding function and returns its result.

    Args:
        tool_call (Dict[str, Any]): A single tool call block from an Anthropic response
        functions (List[Callable]): List of available functions that can be called

    Returns:
        Any: The raw result from calling the function
    """
    # Create a map of function names to functions
    function_map = {f.__name__: f for f in functions}

    tool_name = tool_call.get("name")
    tool_input = tool_call.get("input", {})

    # Call the function if it exists
    if tool_name in function_map:
        if asyncio.iscoroutinefunction(function_map[tool_name]):
            return await function_map[tool_name](**tool_input)
        else:
            return function_map[tool_name](**tool_input)
    else:
        raise f"Tool {tool_name} not found"


class AgentClient:
    def __init__(
        self,
        model: str = "claude-3-5-sonnet-latest",
        functions: List[Callable] = [],
        max_tokens: int = 4096,
        enable_thinking: bool = True,
    ):
        self.model = model
        self.functions = functions
        self.max_tokens = max_tokens
        self.client = AsyncAnthropic()

        # ? https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
        self.thinking_config = self._get_thinking_config(enable_thinking)

    def _get_thinking_config(self, enable_thinking: bool) -> Dict[str, Any]:
        """
        Returns the thinking config for the agent.
        """
        DEFAULT_BUDGET_TOKENS = 16000
        enabled_config = {
            "type": "enabled",
            "budget_tokens": 16000,  # default budget tokens (must be less than max tokens)
        }
        disabled_config = {
            "type": "disabled",
        }

        if enable_thinking and self.max_tokens < DEFAULT_BUDGET_TOKENS:
            shared_error_console.print(
                f"[red]Max tokens must be greater than {DEFAULT_BUDGET_TOKENS}[/red]"
            )
            raise ValueError("Max tokens must be greater than 16000")

        if enable_thinking:  # thinking enabled but invalid model
            if "3-7" not in self.model:
                shared_error_console.print(
                    f"[red]Thinking is not supported for model {self.model}[/red]"
                )
                return disabled_config
            else:
                return enabled_config
        else:  # no thinking enabled
            return disabled_config

    def _get_system_message(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[str, List[Dict[str, Any]]]:
        system_message = next(
            (message for message in messages if message.get("role") == "system"), None
        )
        other_messages = [
            message for message in messages if message.get("role") != "system"
        ]
        return (
            "" if system_message is None else system_message.get("content", "")
        ), other_messages

    async def completion(self, messages: List[Dict[str, Any]]) -> Message:
        system, messages = self._get_system_message(messages)
        response = await self.client.messages.create(
            model=self.model,
            messages=messages,
            system=DEFAULT_SYSTEM_PROMPT + system,
            max_tokens=self.max_tokens,
            tools=[function_to_json_anthropic(f) for f in self.functions],
            tool_choice={"type": "auto"},
            thinking=self.thinking_config
        )
        return response

    async def stream_completion(
        self, messages: List[Dict[str, Any]]
    ) -> AsyncStream[RawMessageStreamEvent]:
        system, messages = self._get_system_message(messages)
        return await self.client.messages.create(
            model=self.model,
            messages=messages,
            system=DEFAULT_SYSTEM_PROMPT + system,
            max_tokens=self.max_tokens,
            stream=True,
            tools=[function_to_json_anthropic(f) for f in self.functions],
            tool_choice={"type": "auto"},
            thinking=self.thinking_config
        )

class Agent:
    def __init__(
        self,
        model: str = "claude-3-5-sonnet-latest",
        functions: List[Callable] = [],
        max_tokens: int = 32000,
        enable_thinking: bool = False,
        debug: bool = False,
    ):
        self.client = AgentClient(
            model=model,
            functions=functions,
            max_tokens=max_tokens,
            enable_thinking=enable_thinking,
        )
        self.functions = functions
        self.debug = debug

    def _print_debug(self, *args, **kwargs):
        if self.debug:
            shared_console.print("[red][DEBUG][/red]", end=" ")
            shared_console.print(*args, **kwargs)

    async def run_iteration(
        self, messages: List[Dict[str, Any]], *args, **kwargs
    ) -> Tuple[List[Dict[str, Any]], bool]:

        self._print_debug("Calling client.stream_completion...")
        stream = await self.client.stream_completion(messages, *args, **kwargs)

        self._print_debug("Stream created")

        # Variables to track tool use
        current_tool_name = None
        current_tool_input_json = ""
        current_tool_input = {}

        # Buffers
        text_buffer = ""  # text buffer to get assistant message
        thinking_buffer = ""  # thinking buffer to get extended thinking

        # Flags
        tool_used = False
        message_done_streaming = False

        # Copy of messages to update
        updated_messages = messages.copy()

        # Process the stream
        try:
            async for event in stream:
                # ? See https://docs.anthropic.com/en/api/messages-streaming
                event_type = event.type
                if event_type == "content_block_start":
                    self._print_debug("Content block start")
                    start_event: RawContentBlockStartEvent = cast(
                        RawContentBlockStartEvent, event
                    )
                    # match the type of the content block
                    match start_event.content_block.type:
                        case "tool_use":
                            self._print_debug("Tool use content block start")
                            current_tool_name = start_event.content_block.name
                        case "text":
                            # Reset text buffer when (if) a new text block starts
                            text_buffer = start_event.content_block.text
                        case "thinking":
                            # Reset thinking buffer when (if) a new thinking block starts
                            thinking_buffer = start_event.content_block.thinking
                        case "redacted_thinking":
                            # ? https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#example-streaming-with-redacted-thinking
                            shared_console.print(
                                "[italic yellow]Received a redacted thinking block.... Wonder what Anthropic is up to...[/italic yellow]",
                                end="",
                            )

                elif event_type == "content_block_delta":
                    delta_event: RawContentBlockDeltaEvent = cast(
                        RawContentBlockDeltaEvent, event
                    )
                    if delta_event.delta.type == "input_json_delta":
                        delta: InputJSONDelta = cast(InputJSONDelta, delta_event.delta)
                        current_tool_input_json += delta.partial_json

                        # Try to parse the complete JSON if it looks complete
                        if (
                            current_tool_input_json.strip()
                            and current_tool_input_json.strip()[-1] == "}"
                        ):
                            try:
                                current_tool_input = json.loads(current_tool_input_json)
                            except json.JSONDecodeError:
                                pass
                    elif delta_event.delta.type == "text_delta":
                        if len(thinking_buffer) > 0:
                            print("\n", end="") # newline in between thinking and text
                        delta: TextDelta = cast(TextDelta, delta_event.delta)
                        shared_console.print(
                            delta.text, end=""
                        )  # print the text as it comes in
                        text_buffer += delta.text  # accumulate the text
                    elif delta_event.delta.type == "thinking_delta":
                        delta: ThinkingDelta = cast(ThinkingDelta, delta_event.delta)
                        shared_console.print(
                            f"[italic blue]{delta.thinking}[/italic blue]", end=""
                        )
                        thinking_buffer += delta.thinking

                elif event_type == "content_block_stop":
                    self._print_debug("Content block stop")
                    stop_event: RawContentBlockStopEvent = cast(
                        RawContentBlockStopEvent, event
                    )
                    if (
                        text_buffer != ""
                    ):  # if we've accumulated any text, add it to the messages
                        print("\n", end="") # print a new line since we finished the block
                        updated_messages.append(
                            {
                                "role": "assistant",
                                "content": text_buffer,
                            }
                        )

                elif event_type == "message_delta":
                    self._print_debug("Message delta")
                    delta_event: RawMessageDeltaEvent = cast(
                        RawMessageDeltaEvent, event
                    )
                    if delta_event.delta.stop_reason == "tool_use":
                        tool_used = True
                        if current_tool_name and current_tool_input:
                            # Execute the tool
                            with shared_console.status(
                                f"[yellow]Executing tool:[/yellow] [green]{current_tool_name}[/green]"
                            ):
                                shared_console.print(
                                    f"[yellow]Input:[/yellow] [green]{current_tool_input}[/green]"
                                )
                                tool_call = {
                                    "name": current_tool_name,
                                    "input": current_tool_input,
                                }
                                result = await handle_tool_call(
                                    tool_call, self.functions
                                )
                                self.tool_counts[
                                    current_tool_name
                                ] += 1  # update tool counts

                            # Format the result as a simple text message
                            tool_result_str = (
                                json.dumps(result)
                                if isinstance(result, dict)
                                else str(result)
                            )
                            tool_response_message = {
                                "role": "user",
                                "content": f"Executed {current_tool_name} with this input: {current_tool_input} and got this result: {tool_result_str}.",
                            }

                            breakout_message = {
                                "role": "user",
                                "content": f"Are you ready to answer my original request? Or do you want to keep calling tools? If you are ready to answer, do it! If not, keep calling tools. DO NOT stop calling tools WIHTOUT answering my original request",
                            }

                            # Add the tool response to messages
                            shared_console.print(
                                f"[yellow]Appended tool response to messages:[/yellow] [green]{tool_response_message}[/green]"
                            )
                            updated_messages.append(tool_response_message)
                            updated_messages.append(breakout_message) # ! breakout message
                            # Reset tool tracking
                            current_tool_name = None
                            current_tool_input_json = ""
                            current_tool_input = {}
                            break  # Break out of the stream loop

                elif event_type == "content_block_stop":
                    self._print_debug("Content block stop")
                    stop_event: RawContentBlockStopEvent = cast(
                        RawContentBlockStopEvent, event
                    )
                    pass

                elif event_type == "message_stop": # ! this only happens when no tool is used
                    self._print_debug("Message stop")
                    stop_event: RawMessageStopEvent = cast(
                        RawMessageStopEvent, event
                    )
                    self._print_debug("Setting message_done_streaming to True")
                    message_done_streaming = True

                elif event_type == "error": # not sure why this isnt getting triggered
                    self._print_debug("Error")
                    error_type: str = event.get("error", {}).get("type", "unknown")
                    error_message: str = event.get("error", {}).get("message", "None")
                    shared_error_console.print(f"[red]\nError: {error_type}\nMessage: {error_message}\n[/red]")

        except Exception as e:
            if issubclass(type(e), AnthropicError): # if error is from anthropic
                print(f"Anthropic Error: {e}. Type: {type(e)} Dir: {dir(e)}")
            else:
                print(f"\nUnhandled exception during streaming: {e}. Type: {type(e)}. Dir: {dir(e)}")
            message_done_streaming = True # break loop gracefully

        # finished = (not tool_used and message_done_streaming) # no tool used, and the message is done 
        # streaming
        finished = (not tool_used) # ! breakout test
        return updated_messages, finished

    async def run(
        self,
        messages: List[Dict[str, Any]],
        max_iterations: int = 10,
    ) -> List[Dict[str, Any]]:

        # get messages, note length of messages
        history = copy.deepcopy(messages)
        init_len = len(history)  # inital number of messages

        # Finished flag
        finished = False  # whether we have finished the task

        # Tool counts
        self.tool_counts = {f.__name__: 0 for f in self.functions}  # reset tool counts
        
        # Print agent configuration
        print_agent_config(max_iterations, list(self.tool_counts.keys()))
        
        while len(history) - init_len < max_iterations * (
            new_messages_per_iteration := 3
        ):
            # we add 2 messages per iteration (user + assistant) so we must check if the history has increased by (num messages per iteration * max iterations)
            history, finished = await self.run_iteration(history)
            if finished:
                print_tool_counts(self.tool_counts)
                return history  # Return the last message
        shared_error_console.print("[red]Max iterations reached[/red]")
        return history
