"""
Python module generated from Java source file org.bukkit.block.data.type.SuspiciousSand

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class SuspiciousSand(BlockData):
    """
    'dusted' represents how far uncovered by brush the block is.
    """

    def getDusted(self) -> int:
        """
        Gets the value of the 'dusted' property.

        Returns
        - the 'dusted' value
        """
        ...


    def setDusted(self, dusted: int) -> None:
        """
        Sets the value of the 'dusted' property.

        Arguments
        - dusted: the new 'dusted' value
        """
        ...


    def getMaximumDusted(self) -> int:
        """
        Gets the maximum allowed value of the 'dusted' property.

        Returns
        - the maximum 'dusted' value
        """
        ...
