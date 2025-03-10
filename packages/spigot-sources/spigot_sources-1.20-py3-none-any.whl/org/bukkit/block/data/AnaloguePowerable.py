"""
Python module generated from Java source file org.bukkit.block.data.AnaloguePowerable

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class AnaloguePowerable(BlockData):
    """
    'power' represents the redstone power level currently being emitted or
    transmitted via this block.
    
    May not be over 9000 or .getMaximumPower() (usually 15).
    """

    def getPower(self) -> int:
        """
        Gets the value of the 'power' property.

        Returns
        - the 'power' value
        """
        ...


    def setPower(self, power: int) -> None:
        """
        Sets the value of the 'power' property.

        Arguments
        - power: the new 'power' value
        """
        ...


    def getMaximumPower(self) -> int:
        """
        Gets the maximum allowed value of the 'power' property.

        Returns
        - the maximum 'power' value
        """
        ...
