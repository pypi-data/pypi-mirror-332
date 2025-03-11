"""
Python module generated from Java source file org.bukkit.block.data.type.Cake

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Cake(BlockData):
    """
    'bites' represents the amount of bites which have been taken from this slice
    of cake.
    
    A value of 0 indicates that the cake has not been eaten, whilst a value of
    .getMaximumBites() indicates that it is all gone :(
    """

    def getBites(self) -> int:
        """
        Gets the value of the 'bites' property.

        Returns
        - the 'bites' value
        """
        ...


    def setBites(self, bites: int) -> None:
        """
        Sets the value of the 'bites' property.

        Arguments
        - bites: the new 'bites' value
        """
        ...


    def getMaximumBites(self) -> int:
        """
        Gets the maximum allowed value of the 'bites' property.

        Returns
        - the maximum 'bites' value
        """
        ...
