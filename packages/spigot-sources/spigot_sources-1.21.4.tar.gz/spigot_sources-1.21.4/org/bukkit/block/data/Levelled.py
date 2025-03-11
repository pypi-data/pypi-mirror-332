"""
Python module generated from Java source file org.bukkit.block.data.Levelled

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Levelled(BlockData):
    """
    'level' represents the amount of fluid contained within this block, either by
    itself or inside a cauldron.
    
    In the case of water and lava blocks the levels have special meanings: a
    level of 0 corresponds to a source block, 1-7 regular fluid heights, and 8-15
    to "falling" fluids. All falling fluids have the same behaviour, but the
    level corresponds to that of the block above them, equal to
    `this.level - 8`
    **Note that counterintuitively, an adjusted level of 1 is the highest level,
    whilst 7 is the lowest.**
    
    May not be higher than .getMaximumLevel().
    """

    def getLevel(self) -> int:
        """
        Gets the value of the 'level' property.

        Returns
        - the 'level' value
        """
        ...


    def setLevel(self, level: int) -> None:
        """
        Sets the value of the 'level' property.

        Arguments
        - level: the new 'level' value
        """
        ...


    def getMaximumLevel(self) -> int:
        """
        Gets the maximum allowed value of the 'level' property.

        Returns
        - the maximum 'level' value
        """
        ...
