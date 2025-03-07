# This file was generated by liblab | https://liblab.com/

from .base import BaseModel
from enum import Enum


class Type_(Enum):
    TOOL_RESULT = "tool_result"

    def list():
        return list(map(lambda x: x.value, Type_._member_map_.values()))


class AnthropicToolCallResults(BaseModel):
    """
    Represents the results of a tool call for Anthropic.
    """

    def __init__(self, type: Type_, content: str, tool_use_id: str, **kwargs):
        """
        Initialize AnthropicToolCallResults
        Parameters:
        ----------
            type: str
            content: str
            tool_use_id: str
        """
        self.type = self._enum_matching(type, Type_.list(), "type")
        self.content = content
        self.tool_use_id = tool_use_id
