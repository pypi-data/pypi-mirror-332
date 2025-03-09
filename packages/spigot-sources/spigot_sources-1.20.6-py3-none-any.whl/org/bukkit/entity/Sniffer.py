"""
Python module generated from Java source file org.bukkit.entity.Sniffer

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Sniffer(Animals):
    """
    Represents a Sniffer.
    """

    def getExploredLocations(self) -> Iterable["Location"]:
        """
        Gets the locations explored by the sniffer.
        
        **Note:** the returned locations use sniffer's current world.

        Returns
        - a collection of locations
        """
        ...


    def removeExploredLocation(self, location: "Location") -> None:
        """
        Remove a location of the explored locations.
        
        **Note:** the location must be in the sniffer's current world for this
        method to have any effect.

        Arguments
        - location: the location to remove

        See
        - .getExploredLocations()
        """
        ...


    def addExploredLocation(self, location: "Location") -> None:
        """
        Add a location to the explored locations.
        
        **Note:** the location must be in the sniffer's current world for this
        method to have any effect.

        Arguments
        - location: the location to add

        See
        - .getExploredLocations()
        """
        ...


    def getState(self) -> "Sniffer.State":
        """
        Get the current state of the sniffer.

        Returns
        - the state of the sniffer
        """
        ...


    def setState(self, state: "Sniffer.State") -> None:
        """
        Set a new state for the sniffer.
        
        This will also make the sniffer make the transition to the new state.

        Arguments
        - state: the new state
        """
        ...


    def findPossibleDigLocation(self) -> "Location":
        """
        Try to get a possible location where the sniffer can dig.

        Returns
        - a Location if found or null
        """
        ...


    def canDig(self) -> bool:
        """
        Gets whether the sniffer can dig in the current Location below
        its head.

        Returns
        - `True` if can dig or `False` otherwise
        """
        ...


    class State(Enum):
        """
        Represents the current state of the Sniffer.
        """

        IDLING = 0
        FEELING_HAPPY = 1
        SCENTING = 2
        SNIFFING = 3
        SEARCHING = 4
        DIGGING = 5
        RISING = 6
