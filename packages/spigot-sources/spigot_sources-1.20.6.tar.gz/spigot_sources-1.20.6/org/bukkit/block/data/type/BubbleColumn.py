"""
Python module generated from Java source file org.bukkit.block.data.type.BubbleColumn

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class BubbleColumn(BlockData):
    """
    'drag' indicates whether a force will be applied on entities moving through
    this block.
    """

    def isDrag(self) -> bool:
        """
        Gets the value of the 'drag' property.

        Returns
        - the 'drag' value
        """
        ...


    def setDrag(self, drag: bool) -> None:
        """
        Sets the value of the 'drag' property.

        Arguments
        - drag: the new 'drag' value
        """
        ...
