"""
Python module generated from Java source file org.bukkit.block.data.type.PistonHead

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class PistonHead(TechnicalPiston):
    """
    'short' denotes this piston head is shorter than the usual amount because it
    is currently retracting.
    """

    def isShort(self) -> bool:
        """
        Gets the value of the 'short' property.

        Returns
        - the 'short' value
        """
        ...


    def setShort(self, _short: bool) -> None:
        """
        Sets the value of the 'short' property.

        Arguments
        - _short: the new 'short' value
        """
        ...
