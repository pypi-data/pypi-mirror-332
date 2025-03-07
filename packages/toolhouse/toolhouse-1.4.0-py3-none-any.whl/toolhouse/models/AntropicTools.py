# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .FunctionParameters import FunctionParameters


class AntropicTools(BaseModel):
    """
    Anthropic Tools
    """

    def __init__(
        self,
        description: str,
        name: str,
        input_schema: FunctionParameters = None,
        **kwargs,
    ):
        """
        Initialize AntropicTools
        Parameters:
        ----------
            description: str
            name: str
            input_schema: FunctionParameters
        """
        self.description = description
        self.name = name
        self.input_schema = input_schema
