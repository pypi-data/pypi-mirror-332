"""
Python module generated from Java source file org.bukkit.block.data.type.Leaves

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Leaves(Waterlogged):
    """
    'persistent' indicates whether or not leaves will be checked by the server to
    see if they are subject to decay or not.
    
    'distance' denotes how far the block is from a tree and is used in
    conjunction with 'persistent' flag to determine if the leaves will decay or
    not.
    """

    def isPersistent(self) -> bool:
        """
        Gets the value of the 'persistent' property.

        Returns
        - the persistent value
        """
        ...


    def setPersistent(self, persistent: bool) -> None:
        """
        Sets the value of the 'persistent' property.

        Arguments
        - persistent: the new 'persistent' value
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
