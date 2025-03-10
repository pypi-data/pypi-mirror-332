"""
Python module generated from Java source file org.bukkit.block.data.type.SeaPickle

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class SeaPickle(Waterlogged):
    """
    'pickles' indicates the number of pickles in this block.
    """

    def getPickles(self) -> int:
        """
        Gets the value of the 'pickles' property.

        Returns
        - the 'pickles' value
        """
        ...


    def setPickles(self, pickles: int) -> None:
        """
        Sets the value of the 'pickles' property.

        Arguments
        - pickles: the new 'pickles' value
        """
        ...


    def getMinimumPickles(self) -> int:
        """
        Gets the minimum allowed value of the 'pickles' property.

        Returns
        - the minimum 'pickles' value
        """
        ...


    def getMaximumPickles(self) -> int:
        """
        Gets the maximum allowed value of the 'pickles' property.

        Returns
        - the maximum 'pickles' value
        """
        ...
