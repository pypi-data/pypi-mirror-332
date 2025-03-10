"""
Python module generated from Java source file org.bukkit.block.data.type.BrewingStand

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class BrewingStand(BlockData):
    """
    Interface to the 'has_bottle_0', 'has_bottle_1', 'has_bottle_2' flags on a
    brewing stand which indicate which bottles are rendered on the outside.
    
    Stand may have 0, 1... .getMaximumBottles()-1 bottles.
    """

    def hasBottle(self, bottle: int) -> bool:
        """
        Checks if the stand has the following bottle

        Arguments
        - bottle: to check

        Returns
        - if bottle is present
        """
        ...


    def setBottle(self, bottle: int, has: bool) -> None:
        """
        Set whether the stand has this bottle present.

        Arguments
        - bottle: to set
        - has: bottle
        """
        ...


    def getBottles(self) -> set["Integer"]:
        """
        Get the indexes of all the bottles present on this block.

        Returns
        - set of all bottles
        """
        ...


    def getMaximumBottles(self) -> int:
        """
        Get the maximum amount of bottles present on this stand.

        Returns
        - maximum bottle count
        """
        ...
