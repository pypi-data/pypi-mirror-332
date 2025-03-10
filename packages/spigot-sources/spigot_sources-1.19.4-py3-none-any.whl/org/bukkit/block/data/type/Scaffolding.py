"""
Python module generated from Java source file org.bukkit.block.data.type.Scaffolding

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Scaffolding(Waterlogged):
    """
    'bottom' indicates whether the scaffolding is floating or not.
    
    'distance' indicates the distance from a scaffolding block placed above a
    'bottom' scaffold.
    
    When 'distance' reaches .getMaximumDistance() the block will drop.
    """

    def isBottom(self) -> bool:
        """
        Gets the value of the 'bottom' property.

        Returns
        - the 'bottom' value
        """
        ...


    def setBottom(self, bottom: bool) -> None:
        """
        Sets the value of the 'bottom' property.

        Arguments
        - bottom: the new 'bottom' value
        """
        ...


    def getDistance(self) -> int:
        """
        Gets the value of the 'distance' property.

        Returns
        - the 'distance' value
        """
        ...


    def setDistance(self, distance: int) -> None:
        """
        Sets the value of the 'distance' property.

        Arguments
        - distance: the new 'distance' value
        """
        ...


    def getMaximumDistance(self) -> int:
        """
        Gets the maximum allowed value of the 'distance' property.

        Returns
        - the maximum 'distance' value
        """
        ...
