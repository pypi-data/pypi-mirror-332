"""
Python module generated from Java source file org.bukkit.block.data.Lightable

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Lightable(BlockData):
    """
    'lit' denotes whether this block (either a redstone torch or furnace) is
    currently lit - that is not burned out.
    """

    def isLit(self) -> bool:
        """
        Gets the value of the 'lit' property.

        Returns
        - the 'lit' value
        """
        ...


    def setLit(self, lit: bool) -> None:
        """
        Sets the value of the 'lit' property.

        Arguments
        - lit: the new 'lit' value
        """
        ...
