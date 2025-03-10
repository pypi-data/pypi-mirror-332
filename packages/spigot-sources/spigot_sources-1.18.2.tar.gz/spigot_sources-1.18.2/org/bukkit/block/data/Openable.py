"""
Python module generated from Java source file org.bukkit.block.data.Openable

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Openable(BlockData):
    """
    'open' denotes whether this door-like block is currently opened.
    """

    def isOpen(self) -> bool:
        """
        Gets the value of the 'open' property.

        Returns
        - the 'open' value
        """
        ...


    def setOpen(self, open: bool) -> None:
        """
        Sets the value of the 'open' property.

        Arguments
        - open: the new 'open' value
        """
        ...
