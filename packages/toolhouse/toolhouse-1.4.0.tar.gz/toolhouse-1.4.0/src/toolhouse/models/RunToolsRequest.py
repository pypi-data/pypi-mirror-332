# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .base import BaseModel
from typing import Any
from typing import Union
from .AnthropicToolCall import AnthropicToolCall
from .OpenAiAssistantsToolCall import OpenAiAssistantsToolCall
from .OpenAiToolCall import OpenAiToolCall
from .GenericToolCall import GenericToolCall
from .Provider import Provider


def returnAnthropicToolCall(input_data):
    return AnthropicToolCall(**input_data)


def returnOpenAiAssistantsToolCall(input_data):
    return OpenAiAssistantsToolCall(**input_data)


def returnOpenAiToolCall(input_data):
    return OpenAiToolCall(**input_data)


def returnGenericToolCall(input_data):
    return GenericToolCall(**input_data)


class ContentGuard(BaseModel):
    required_lists: dict = {
        "AnthropicToolCall": ["id", "input_", "name", "type"],
        "OpenAiAssistantsToolCall": ["id", "function", "type"],
        "OpenAiToolCall": ["id", "function"],
        "GenericToolCall": ["input", "name"],
    }
    optional_lists: dict = {
        "AnthropicToolCall": [],
        "OpenAiAssistantsToolCall": [],
        "OpenAiToolCall": [],
        "GenericToolCall": [],
    }
    class_list: dict = {
        "AnthropicToolCall": returnAnthropicToolCall,
        "OpenAiAssistantsToolCall": returnOpenAiAssistantsToolCall,
        "OpenAiToolCall": returnOpenAiToolCall,
        "GenericToolCall": returnGenericToolCall,
    }

    @classmethod
    def return_one_of(cls, raw_input):
        return cls._one_of(
            cls.required_lists, cls.optional_lists, cls.class_list, raw_input
        )


Content = Union[AnthropicToolCall, OpenAiAssistantsToolCall, OpenAiToolCall, GenericToolCall]


class RunToolsRequest(BaseModel):
    """
    Represents a tool call for Toolhouse.
    """

    def __init__(self, content: Content, provider: Provider, metadata: Any, bundle: str):
        """
        Initialize RunToolsRequest
        Parameters:
        ----------
            content: Content
            provider: str
            metadata: dict
        """
        self.content = content
        self.provider = self._enum_matching(provider, Provider.list(), "provider")
        self.metadata = metadata
        self.bundle = bundle
