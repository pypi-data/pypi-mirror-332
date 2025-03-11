"""
Python module generated from Java source file org.bukkit.block.data.type.CreakingHeart

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Orientable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class CreakingHeart(Orientable):
    """
    'active' is whether the block is active.
    
    'natural' is whether this is a naturally generated block.
    """

    def isActive(self) -> bool:
        """
        Gets the value of the 'active' property.

        Returns
        - the 'active' value
        """
        ...


    def setActive(self, active: bool) -> None:
        """
        Sets the value of the 'active' property.

        Arguments
        - active: the new 'active' value
        """
        ...


    def isNatural(self) -> bool:
        """
        Gets the value of the 'natural' property.

        Returns
        - the 'natural' value
        """
        ...


    def setNatural(self, natural: bool) -> None:
        """
        Sets the value of the 'natural' property.

        Arguments
        - natural: the new 'natural' value
        """
        ...
