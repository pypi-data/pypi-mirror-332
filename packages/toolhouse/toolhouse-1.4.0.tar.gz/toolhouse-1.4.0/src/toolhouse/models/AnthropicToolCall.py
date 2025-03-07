# This file was generated by liblab | https://liblab.com/

from .base import BaseModel
from typing import Any
from enum import Enum


class Type_(Enum):
    TOOL_USE = "tool_use"

    def list():
        return list(map(lambda x: x.value, Type_._member_map_.values()))


class AnthropicToolCall(BaseModel):
    """
    Represents a tool call for Anthropic.
    """

    def __init__(self, type: Type_, input: Any, name: str, id: str, **kwargs):
        """
        Initialize AnthropicToolCall
        Parameters:
        ----------
            type: str
            input
            name: str
            id: str
        """
        self.type = self._enum_matching(type, Type_.list(), "type")
        self.input = input
        self.name = name
        self.id = id
