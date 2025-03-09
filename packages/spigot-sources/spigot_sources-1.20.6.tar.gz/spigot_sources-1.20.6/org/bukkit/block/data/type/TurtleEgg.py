"""
Python module generated from Java source file org.bukkit.block.data.type.TurtleEgg

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Hatchable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class TurtleEgg(Hatchable):
    """
    'eggs' is the number of eggs which appear in this block.
    """

    def getEggs(self) -> int:
        """
        Gets the value of the 'eggs' property.

        Returns
        - the 'eggs' value
        """
        ...


    def setEggs(self, eggs: int) -> None:
        """
        Sets the value of the 'eggs' property.

        Arguments
        - eggs: the new 'eggs' value
        """
        ...


    def getMinimumEggs(self) -> int:
        """
        Gets the minimum allowed value of the 'eggs' property.

        Returns
        - the minimum 'eggs' value
        """
        ...


    def getMaximumEggs(self) -> int:
        """
        Gets the maximum allowed value of the 'eggs' property.

        Returns
        - the maximum 'eggs' value
        """
        ...
