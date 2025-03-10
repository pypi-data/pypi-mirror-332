"""
Python module generated from Java source file org.bukkit.block.data.Hatchable

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Hatchable(BlockData):
    """
    'hatch' is the number of entities which may hatch from these eggs.
    """

    def getHatch(self) -> int:
        """
        Gets the value of the 'hatch' property.

        Returns
        - the 'hatch' value
        """
        ...


    def setHatch(self, hatch: int) -> None:
        """
        Sets the value of the 'hatch' property.

        Arguments
        - hatch: the new 'hatch' value
        """
        ...


    def getMaximumHatch(self) -> int:
        """
        Gets the maximum allowed value of the 'hatch' property.

        Returns
        - the maximum 'hatch' value
        """
        ...
