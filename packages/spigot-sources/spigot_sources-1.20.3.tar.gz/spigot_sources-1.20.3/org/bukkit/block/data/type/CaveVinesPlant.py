"""
Python module generated from Java source file org.bukkit.block.data.type.CaveVinesPlant

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class CaveVinesPlant(BlockData):
    """
    'berries' indicates whether the block has berries.
    """

    def isBerries(self) -> bool:
        """
        Gets the value of the 'berries' property.

        Returns
        - the 'berries' value
        """
        ...


    def setBerries(self, berries: bool) -> None:
        """
        Sets the value of the 'berries' property.

        Arguments
        - berries: the new 'berries' value
        """
        ...
