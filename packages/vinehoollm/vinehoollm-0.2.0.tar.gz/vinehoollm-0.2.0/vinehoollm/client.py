"""
Main client implementation for VinehooLLM
"""

from typing import Optional, List, Dict, Any, Callable
import json
from openai import OpenAI
from pydantic import BaseModel
import asyncio
from inspect import iscoroutinefunction

from .types import (
    CompletionResponse,
    ChatMessage,
    FunctionCall,
    ToolCall,
    ResponseFormat
)


class VinehooLLM:
    """
    Main client class for interacting with OpenAI-compatible LLMs
    """

    def __init__(
            self,
            api_key: str,
            base_url: str = "https://api.openai.com/v1",
            model: str = "gpt-4o-mini",
            timeout: int = 30,
            tools: Optional[List[Dict[str, Any]]] = None,
            tool_handlers: Optional[Dict[str, Callable]] = None,
    ):
        """
        Initialize the VinehooLLM client
        
        Args:
            api_key: API key for authentication
            base_url: Base URL for the API endpoint
            model: Model identifier to use
            timeout: Request timeout in seconds
            tools: List of tool definitions that the model can use
            tool_handlers: Dictionary mapping tool names to their handler functions
        """
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
        )
        self.model = model
        self.tools = tools or []
        self.tool_handlers = tool_handlers or {}

    async def _handle_function_call(self, function_call: FunctionCall) -> str:
        """
        Handle a function call from the model
        
        Args:
            function_call: The function call to handle
            
        Returns:
            The result of the function call as a string
        """
        if function_call.name not in self.tool_handlers:
            raise ValueError(f"No handler found for function {function_call.name}")

        handler = self.tool_handlers[function_call.name]
        try:
            args = json.loads(function_call.arguments)
            if iscoroutinefunction(handler):
                result = await handler(**args)
            else:
                result = handler(**args)
            return str(result)
        except Exception as e:
            return f"Error executing function {function_call.name}: {str(e)}"

    def chat(
            self,
            messages: List[ChatMessage],
            temperature: float = 0.7,
            auto_handle_functions: bool = True,
            response_format: Optional[ResponseFormat] = None,
            **kwargs: Any,
    ) -> CompletionResponse:
        """
        Generate chat completion for a conversation
        
        Args:
            messages: List of chat messages
            temperature: Sampling temperature (0-1)
            auto_handle_functions: Whether to automatically handle function calls
            response_format: Format to return the response in
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            CompletionResponse object containing the generated text
        """
        formatted_messages = []
        for msg in messages:
            message_dict = {
                "role": msg.role,
                "content": msg.content
            }
            if msg.tool_calls:
                message_dict["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in msg.tool_calls
                ]
            if msg.tool_call_id:
                message_dict["tool_call_id"] = msg.tool_call_id
            formatted_messages.append(message_dict)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=formatted_messages,
            temperature=temperature,
            tools=self.tools if self.tools else None,
            response_format=response_format,
            **kwargs,
        )

        choice = response.choices[0]
        function_call = None
        text = choice.message.content or ""

        if hasattr(choice.message, 'tool_calls') and choice.message.tool_calls:
            # Add the assistant's response with tool calls to messages
            tool_calls_data = [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                } for tool_call in choice.message.tool_calls
            ]

            assistant_message = {
                "role": "assistant",
                "content": None,
                "tool_calls": tool_calls_data
            }
            formatted_messages.append(assistant_message)

            results = []
            for tool_call in choice.message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                if auto_handle_functions:
                    result = self._handle_function_call(FunctionCall(name=name, arguments=tool_call.function.arguments))
                    formatted_messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
                    results.append(result)
                else:
                    function_call = FunctionCall(name=name, arguments=tool_call.function.arguments)

            if auto_handle_functions and results:
                # Get final response after tool calls
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=formatted_messages,
                    temperature=temperature,
                    tools=self.tools if self.tools else None,
                    response_format=response_format,
                    **kwargs,
                )
                text = response.choices[0].message.content or ""

        # Flatten the usage statistics to only include top-level integer values
        usage_stats = {}
        raw_usage = response.usage.model_dump()
        for key, value in raw_usage.items():
            if isinstance(value, int):
                usage_stats[key] = value

        # Add the final assistant response to messages if it has content
        if text:
            formatted_messages.append({
                "role": "assistant",
                "content": text
            })

        return CompletionResponse(
            text=text,
            finish_reason=choice.finish_reason,
            usage=usage_stats,
            function_call=function_call,
            messages=[ChatMessage(**msg) for msg in formatted_messages],
        )

    @staticmethod
    def format_messages_to_json(messages: List[ChatMessage]) -> str:
        """
        Convert a list of ChatMessage objects to a JSON string
        
        Args:
            messages: List of chat messages
            
        Returns:
            JSON string representation of the messages
        """
        formatted_messages = []
        for msg in messages:
            message_dict = {
                "role": msg.role,
                "content": msg.content
            }
            if msg.tool_calls:
                message_dict["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in msg.tool_calls
                ]
            if msg.tool_call_id:
                message_dict["tool_call_id"] = msg.tool_call_id
            formatted_messages.append(message_dict)

        return json.dumps(formatted_messages, ensure_ascii=False, indent=2)

    @staticmethod
    def parse_messages_from_json(json_str: str) -> List[ChatMessage]:
        """
        Convert a JSON string to a list of ChatMessage objects
        
        Args:
            json_str: JSON string representation of messages
            
        Returns:
            List of ChatMessage objects
        """
        messages_data = json.loads(json_str)
        return [ChatMessage(**msg) for msg in messages_data]

    async def chat_async(
            self,
            messages: List[ChatMessage],
            temperature: float = 0.7,
            auto_handle_functions: bool = True,
            response_format: Optional[ResponseFormat] = None,
            **kwargs: Any,
    ) -> CompletionResponse:
        """
        Generate chat completion for a conversation asynchronously
        
        Args:
            messages: List of chat messages
            temperature: Sampling temperature (0-1)
            auto_handle_functions: Whether to automatically handle function calls
            response_format: Format to return the response in
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            CompletionResponse object containing the generated text
        """
        formatted_messages = []
        for msg in messages:
            message_dict = {
                "role": msg.role,
                "content": msg.content
            }
            if msg.tool_calls:
                message_dict["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in msg.tool_calls
                ]
            if msg.tool_call_id:
                message_dict["tool_call_id"] = msg.tool_call_id
            formatted_messages.append(message_dict)

        response = await asyncio.to_thread(self.client.chat.completions.create,
                                           model=self.model,
                                           messages=formatted_messages,
                                           temperature=temperature,
                                           tools=self.tools if self.tools else None,
                                           response_format=response_format,
                                           **kwargs,
                                           )

        choice = response.choices[0]
        function_call = None
        text = choice.message.content or ""
        x = choice
        while x.message.tool_calls is not None and len(x.message.tool_calls) > 0:
            if hasattr(x.message, 'tool_calls') and x.message.tool_calls:
                tool_calls_data = [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in x.message.tool_calls
                ]

                assistant_message = {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": tool_calls_data
                }
                formatted_messages.append(assistant_message)

                results = []

                for tool_call in x.message.tool_calls:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)

                    if auto_handle_functions:
                        result = await self._handle_function_call(
                            FunctionCall(name=name, arguments=tool_call.function.arguments))
                        formatted_messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": result
                        })
                        results.append(result)
                    else:
                        function_call = FunctionCall(name=name, arguments=tool_call.function.arguments)

                if auto_handle_functions and results:
                    response = await asyncio.to_thread(self.client.chat.completions.create,
                                                       model=self.model,
                                                       messages=formatted_messages,
                                                       temperature=temperature,
                                                       tools=self.tools if self.tools else None,
                                                       response_format=response_format,
                                                       **kwargs,
                                                       )
                    text = response.choices[0].message.content or ""
                    if len(response.choices) > 0:
                        x = response.choices[0]

        usage_stats = {}
        raw_usage = response.usage.model_dump()
        for key, value in raw_usage.items():
            if isinstance(value, int):
                usage_stats[key] = value

        if text:
            formatted_messages.append({
                "role": "assistant",
                "content": text
            })

        return CompletionResponse(
            text=text,
            finish_reason=choice.finish_reason,
            usage=usage_stats,
            function_call=function_call,
            messages=[ChatMessage(**msg) for msg in formatted_messages],
        )
