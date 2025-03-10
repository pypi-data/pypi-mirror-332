"""
Python module generated from Java source file org.bukkit.block.EndGateway

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class EndGateway(TileState):
    """
    Represents a captured state of an end gateway.
    """

    def getExitLocation(self) -> "Location":
        """
        Gets the location that entities are teleported to when
        entering the gateway portal.
        
        If this block state is not placed the location's world will be null.

        Returns
        - the gateway exit location
        """
        ...


    def setExitLocation(self, location: "Location") -> None:
        """
        Sets the exit location that entities are teleported to when
        they enter the gateway portal.
        
        If this block state is not placed the location's world has to be null.

        Arguments
        - location: the new exit location

        Raises
        - IllegalArgumentException: for differing worlds
        """
        ...


    def isExactTeleport(self) -> bool:
        """
        Gets whether this gateway will teleport entities directly to
        the exit location instead of finding a nearby location.

        Returns
        - True if the gateway is teleporting to the exact location
        """
        ...


    def setExactTeleport(self, exact: bool) -> None:
        """
        Sets whether this gateway will teleport entities directly to
        the exit location instead of finding a nearby location.

        Arguments
        - exact: whether to teleport to the exact location
        """
        ...


    def getAge(self) -> int:
        """
        Gets the age in ticks of the gateway.
        
        If the age is less than 200 ticks a magenta beam will be emitted, whilst
        if it is a multiple of 2400 ticks a purple beam will be emitted.

        Returns
        - age in ticks
        """
        ...


    def setAge(self, age: int) -> None:
        """
        Sets the age in ticks of the gateway.
        
        If the age is less than 200 ticks a magenta beam will be emitted, whilst
        if it is a multiple of 2400 ticks a purple beam will be emitted.

        Arguments
        - age: new age in ticks
        """
        ...
