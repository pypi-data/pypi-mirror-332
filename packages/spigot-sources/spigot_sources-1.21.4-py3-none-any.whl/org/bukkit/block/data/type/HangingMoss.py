"""
Python module generated from Java source file org.bukkit.block.data.type.HangingMoss

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class HangingMoss(BlockData):
    """
    'tip' indicates whether this block is a tip.
    """

    def isTip(self) -> bool:
        """
        Gets the value of the 'tip' property.

        Returns
        - the 'tip' value
        """
        ...


    def setTip(self, tip: bool) -> None:
        """
        Sets the value of the 'tip' property.

        Arguments
        - tip: the new 'tip' value
        """
        ...
