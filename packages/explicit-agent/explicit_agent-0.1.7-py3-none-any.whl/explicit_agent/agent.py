import json
from typing import Optional, List, Any, Type, Dict, Literal

from openai import OpenAI
from rich.console import Console
from rich.pretty import pprint
import logging

from .tools import register_tools, StopTool, BaseTool


class ExplicitAgent:
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        initial_state: Optional[Any] = {},
        verbose: Optional[Literal[None, "basic", "detailed"]] = "basic",
    ):
        """
        Initialize the ExplicitAgent with the given API key, base URL, and model.
        This uses the OpenAI API.

        Args:
            `api_key`: The API key for the provider (e.g. OpenAI, OpenRouter, Anthropic, etc.).
            `base_url`: The base URL for the provider (e.g. OpenAI, OpenRouter, Anthropic, etc.).
            `initial_state`: Optional initial state for the agent. Must be a mutable object (e.g., dict, list).
            `verbose`: Whether to print verbose output to the console. Can be `None` (no verbose output), `"basic"` (basic verbose output), or `"detailed"` (detailed verbose output). Default is `"basic"`.
        """

        if initial_state is not None:
            try:
                hash(initial_state)
                raise ValueError(
                    f"Initial state must be mutable. Got immutable type: {type(initial_state)}. "
                    "Use a mutable type like dict, list, or a custom class instead."
                )
            except TypeError:
                pass

        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url=base_url,
            )
        except Exception as e:
            self.logger.error(f"Error initializing OpenAI client: {e}")
            raise

        if verbose not in [None, "basic", "detailed"]:
            raise ValueError("Verbose must be None, 'basic', or 'detailed'")

        self.verbose = verbose

        self.console = Console()
        self.logger = logging.getLogger("explicit_agent")

        self.messages: List[Dict[str, Any]] = []

        self.state: Any = initial_state

    def _process_tool_calls(self, tool_calls, tools) -> bool:
        """
        Process multiple tool calls and execute them sequentially.

        Args:
            `tool_calls`: List of tool calls from the LLM response.
            `tools`: Dictionary mapping tool classes to their OpenAI definitions.

        Returns:
            `bool`: Whether to stop execution of the agent.
        """
        for tool_call in tool_calls:
            tool_name = tool_call.function.name

            tool_class = next(
                (tool for tool in tools.keys() if tool.__name__ == tool_name), None
            )

            if not tool_class:
                self._handle_tool_error(tool_call.id, f"Unknown tool: '{tool_name}'")
                continue

            try:
                tool_args = json.loads(tool_call.function.arguments)
                tool_instance = tool_class(**tool_args)
            except Exception as e:
                self._handle_tool_error(
                    tool_call.id,
                    f"Invalid tool arguments for '{tool_name}' tool.\nGiven arguments: {tool_call.function.arguments}\nError: {e}",
                )
                continue

            self.logger.info(f"Tool Call: {tool_name}({tool_args})")
            if self.verbose:
                self.console.print(
                    f"[bold blue]Tool Call:[/bold blue] {tool_name}({tool_args})"
                )

            try:
                is_stop_tool = issubclass(tool_class, StopTool)
                is_stateful = tool_class.is_stateful()

                if is_stateful:
                    result = tool_instance.execute(state=self.state)
                else:
                    result = tool_instance.execute()

                try:
                    serialized_result = json.dumps({"result": result})
                except (TypeError, ValueError) as e:
                    self.logger.warning(
                        f"Non-serializable result type: {type(result)}. Converting to string."
                    )
                    serialized_result = json.dumps({"result": str(result)})

                tool_call_response = {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": serialized_result,
                }

                self.messages.append(tool_call_response)

                self.logger.info(f"Tool Call Result: {tool_name}(...) -> {result}")
                if self.verbose:
                    if self.verbose == "basic":
                        self.console.print(
                            f"[bold blue]Tool Call Result:[/bold blue] {tool_name}(...) ->"
                        )
                        pprint(result, console=self.console, expand_all=True, max_length=20)
                    else:
                        self.console.print(
                            f"[bold blue]Tool Call Result:[/bold blue] {tool_name}(...) ->"
                        )
                        pprint(result, console=self.console, expand_all=True, max_length=20)

                self.logger.info(f"State: {self.state}")
                if self.verbose and self.state:
                    if self.verbose == "basic":
                        self.console.print(
                            f"[bold blue]State:[/bold blue]"
                        )
                        pprint(self.state, console=self.console, expand_all=True, max_length=20)
                    else:
                        self.console.print("[bold blue]State:[/bold blue]")
                        pprint(self.state, console=self.console, expand_all=True)

                if is_stop_tool:
                    self.logger.info("Agent execution complete")
                    if self.verbose:
                        self.console.print(
                            "[bold bright_green]Agent execution complete[/bold bright_green]"
                        )
                    return True

            except Exception as e:
                self._handle_tool_error(
                    tool_call.id,
                    f"Error executing '{tool_name}' tool: {str(e)}",
                )
                continue

        return False

    def _handle_tool_error(self, tool_call_id: str, error_msg: str) -> None:
        """
        Handle and log tool execution errors.

        Args:
            `tool_call_id`: The ID of the tool call.
            `error_msg`: The error message.
        """

        self.logger.error(error_msg)
        if self.verbose:
            self.console.print(f"[bold red1]{error_msg}[/bold red1]")
        self.messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": json.dumps({"error": error_msg}),
            }
        )

    def _display_tool_usage_stats(self, tool_usage_stats: Dict[str, int], total_tool_calls: int) -> None:
        """
        Display tool usage statistics.
        """
        self.console.print("\n[bold blue]Tool Usage Statistics:[/bold blue]")
        for tool_name, count in tool_usage_stats.items():
            percentage = (count / total_tool_calls) * 100 if total_tool_calls > 0 else 0
            self.console.print(f"- {tool_name}: {count} ({percentage:.1f}%)")

    def run(
        self,
        model: str,
        prompt: str,
        system_prompt: Optional[str] = None,
        budget: int = 20,
        tools: Optional[List[Type[BaseTool]]] = None,
        tool_choice: str = "auto",
        parallel_tool_calls: bool = False,
        **kwargs: Any,
    ) -> Any:
        """
        Run the ExplicitAgent with the given prompt and tools.

        Args:
            `model`: The model to use for the agent. The model name format depends on the provider specified during initialization (e.g., "gpt-4o-mini" for OpenAI, "openai/gpt-4o-mini" for OpenRouter, etc.).
            `prompt`: The user's request to process.
            `system_prompt`: Optional system prompt to guide the agent's behavior. If provided, it will replace any existing system prompt in the messages.
            `budget`: The maximum number of steps to run. The agent will stop if it reaches this limit.
            `tools`: List of tool classes. If no tools are provided, the agent will act as a simple chatbot.
            `tool_choice`: The tool choice to use for the agent. Can be `"auto"`, `"required"`, or a specific tool (i.e `{"type": "function", "function": {"name": "get_weather"}}`).
            `parallel_tool_calls`: Whether to allow the model to call multiple functions in parallel.
            `**kwargs`: Additional keyword arguments to pass to the OpenAI API (i.e. `temperature`, `max_tokens`, `reasoning_effort`, etc.).
        Returns:
            `Any`: The final state of the agent.
        """
        try:
            tool_usage_stats: Dict[str, int] = {}
            total_tool_calls: int = 0

            if not model or not isinstance(model, str):
                raise ValueError("Model name must be a non-empty string")

            if not prompt or not isinstance(prompt, str):
                raise ValueError("Prompt must be a non-empty string")

            if not isinstance(budget, int) or budget <= 0:
                raise ValueError("Budget must be a positive integer")

            if tool_choice not in ["auto", "required"] and not isinstance(
                tool_choice, dict
            ):
                raise ValueError(
                    "Tool choice must be 'auto', 'required', or a specific tool configuration"
                )

            if not tools:
                tools = {}
                tool_choice = "auto"
            else:
                for tool in tools:
                    if not issubclass(tool, BaseTool):
                        raise ValueError(
                            f"Tool class '{tool.__name__}' must be a subclass of BaseTool or StopTool"
                        )
                tools = register_tools(tools)

            if system_prompt:
                self.messages = [
                    msg for msg in self.messages if msg.get("role", None) != "system"
                ]
                self.messages.insert(0, {"role": "system", "content": system_prompt})

            self.messages.append({"role": "user", "content": prompt})

            current_step = 0

            while True:
                current_step += 1

                self.logger.info(f"Agent Step {current_step}/{budget}")
                if self.verbose:
                    self.console.rule(
                        f"[bold green_yellow]Agent Step {current_step}/{budget}[/bold green_yellow]",
                        style="green_yellow",
                    )

                if current_step >= budget:
                    warning_msg = f"Warning: The agent has reached the maximum budget of steps without completion (budget: {budget})"
                    self.logger.warning(warning_msg)
                    if self.verbose:
                        self.console.print(
                            f"[bold orange1]{warning_msg}[/bold orange1]"
                        )
                    return self.state

                response = self.client.chat.completions.create(
                    model=model,
                    messages=self.messages,
                    tools=list(tools.values()),
                    tool_choice=tool_choice,
                    parallel_tool_calls=parallel_tool_calls,
                    **kwargs,
                )

                if hasattr(response, "error") and response.error:
                    error_details = response.error
                    error_message = error_details.get("message", "Unknown API error")
                    error_code = error_details.get("code", "unknown")

                    if (
                        "metadata" in error_details
                        and "raw" in error_details["metadata"]
                    ):
                        try:
                            raw_error = json.loads(error_details["metadata"]["raw"])
                            if "error" in raw_error and "message" in raw_error["error"]:
                                error_message = raw_error["error"]["message"]
                        except (json.JSONDecodeError, KeyError):
                            pass

                    error_msg = f"API Error ({error_code}): {error_message}"
                    self.logger.error(error_msg)
                    raise ValueError(error_msg)

                message = response.choices[0].message

                if not message.tool_calls:
                    self.messages.append(message.model_dump())
                    self.logger.info(f"Agent Message: {message.content}")
                    if self.verbose:
                        self.console.print(
                            f"[bold blue]Agent Message:[/bold blue] {message.content}"
                        )
                    continue

                if not parallel_tool_calls and len(message.tool_calls) > 1:
                    self.logger.warning(
                        f"Received {len(message.tool_calls)} tool calls when parallel_tool_calls=False. Processing only the first one."
                    )
                    if self.verbose:
                        self.console.print(
                            f"[yellow]Warning: Received {len(message.tool_calls)} tool calls when parallel_tool_calls=False. Processing only the first one.[/yellow]"
                        )
                    message = message.model_copy(
                        update={"tool_calls": [message.tool_calls[0]]}
                    )

                self.messages.append(message.model_dump())

                tool_calls = message.tool_calls
                
                for tool_call in tool_calls:
                    tool_name = tool_call.function.name
                    tool_usage_stats[tool_name] = tool_usage_stats.get(tool_name, 0) + 1
                    total_tool_calls += 1
                
                done = self._process_tool_calls(tool_calls=tool_calls, tools=tools)

                if done:
                    if self.verbose and tool_usage_stats:
                        self._display_tool_usage_stats(tool_usage_stats, total_tool_calls)
                    
                    return self.state

                if current_step >= budget:
                    warning_msg = f"Warning: The agent has reached the maximum budget of steps without completion (budget: {budget})"
                    self.logger.warning(warning_msg)
                    if self.verbose:
                        self.console.print(
                            f"[bold orange1]{warning_msg}[/bold orange1]"
                        )
                    
                    if self.verbose and tool_usage_stats:
                        self._display_tool_usage_stats(tool_usage_stats, total_tool_calls)
                    
                    return self.state

        except ValueError as e:
            raise

        except Exception as e:
            self.logger.error(f"Unexpected error while running agent: {str(e)}")
            raise RuntimeError(f"Unexpected error while running agent: {str(e)}") from e
