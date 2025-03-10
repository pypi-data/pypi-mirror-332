"""
Python module generated from Java source file org.bukkit.block.data.type.Sapling

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Sapling(BlockData):
    """
    'stage' represents the growth stage of a sapling.
    
    When the sapling reaches .getMaximumStage() it will attempt to grow
    into a tree as the next stage.
    """

    def getStage(self) -> int:
        """
        Gets the value of the 'stage' property.

        Returns
        - the 'stage' value
        """
        ...


    def setStage(self, stage: int) -> None:
        """
        Sets the value of the 'stage' property.

        Arguments
        - stage: the new 'stage' value
        """
        ...


    def getMaximumStage(self) -> int:
        """
        Gets the maximum allowed value of the 'stage' property.

        Returns
        - the maximum 'stage' value
        """
        ...
