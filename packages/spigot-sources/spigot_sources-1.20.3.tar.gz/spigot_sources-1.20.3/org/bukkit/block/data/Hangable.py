"""
Python module generated from Java source file org.bukkit.block.data.Hangable

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Hangable(BlockData):
    """
    'hanging' denotes whether the lantern is hanging from a block.
    """

    def isHanging(self) -> bool:
        """
        Gets the value of the 'hanging' property.

        Returns
        - the 'hanging' value
        """
        ...


    def setHanging(self, hanging: bool) -> None:
        """
        Sets the value of the 'hanging' property.

        Arguments
        - hanging: the new 'hanging' value
        """
        ...
