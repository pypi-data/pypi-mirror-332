import json
from typing import Optional, List, Any, Type, Dict

from openai import OpenAI
from rich.console import Console
import logging

from .tools import register_tools, StopTool, BaseTool


class ExplicitAgent:
    """
    The ExplicitAgent class is a wrapper around the OpenAI API that allows for the execution of tool calls.
    """
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        verbose: bool = False,
    ):
        """
        Initialize the ExplicitAgent with the given API key, base URL, and model.
        This uses the OpenAI API.

        Args:
            `api_key`: The API key for the provider (e.g. OpenAI, OpenRouter, Anthropic, etc.).
            `base_url`: The base URL for the provider (e.g. OpenAI, OpenRouter, Anthropic, etc.).
            `verbose`: Whether to print verbose output to the console. Can be either `True` or `False`. Default is `False`. For more detailed verbose output, it is recommended to use print statements or other verbose methods directly in the implementation of your own agent.
        """
        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url=base_url,
            )
        except Exception as e:
            self.logger.error(f"Error initializing OpenAI client: {e}")
            raise

        self.verbose = verbose

        self.console = Console()
        self.logger = logging.getLogger("explicit_agent")

        self.messages: List[Dict[str, Any]] = []

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
                self._handle_tool_error(
                    tool_call.id, 
                    f"Unknown tool: '{tool_name}'"
                )
                continue

            try:
                arguments_str = tool_call.function.arguments.strip()
                tool_args = json.loads(arguments_str) if arguments_str else {}
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

            is_stop_tool = issubclass(tool_class, StopTool)
            
            try:
                result = tool_instance.execute()
            except Exception as e:
                self._handle_tool_error(
                    tool_call.id, 
                    f"Error executing '{tool_name}' tool: {str(e)}"
                )
                continue

            try:
                serialized_result = json.dumps({"result": result}, indent=4)
            except (TypeError, ValueError) as e:
                self.logger.warning(
                    f"Non-serializable result type: {type(result)}. Converting to string."
                )
                serialized_result = json.dumps({"result": str(result)}, indent=4)

            tool_call_response = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": serialized_result,
            }

            self.messages.append(tool_call_response)

            self.logger.info(f"Tool Call Result: {tool_name}(...) -> {result}")
            if self.verbose:
                self.console.print("[bold blue]Tool Execution Complete[/bold blue]")

            self.console.print()

            if is_stop_tool:
                self.logger.info("Agent execution complete")
                if self.verbose:
                    self.console.print("[bold bright_green]Agent execution complete[/bold bright_green]")
                return True
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
            `bool`: Whether the agent has completed its task.
        """
        try:
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
                
                done = self._process_tool_calls(tool_calls=tool_calls, tools=tools)

                if done:
                    return True
                
                if current_step + 1 >= budget:
                    warning_msg = f"Warning: The agent has reached the maximum budget of steps without completion (budget: {budget})"
                    self.logger.warning(warning_msg)
                    if self.verbose:
                        self.console.print(
                            f"[bold orange1]{warning_msg}[/bold orange1]"
                        )
                    return False

        except ValueError as e:
            raise

        except Exception as e:
            self.logger.error(f"Unexpected error while running agent: {str(e)}")
            raise RuntimeError(f"Unexpected error while running agent: {str(e)}")
