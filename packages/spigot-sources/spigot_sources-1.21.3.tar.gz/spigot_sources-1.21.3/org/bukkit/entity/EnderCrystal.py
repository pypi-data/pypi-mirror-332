"""
Python module generated from Java source file org.bukkit.entity.EnderCrystal

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class EnderCrystal(Entity):
    """
    A crystal that heals nearby EnderDragons
    """

    def isShowingBottom(self) -> bool:
        """
        Return whether or not this end crystal is showing the
        bedrock slate underneath it.

        Returns
        - True if the bottom is being shown
        """
        ...


    def setShowingBottom(self, showing: bool) -> None:
        """
        Sets whether or not this end crystal is showing the
        bedrock slate underneath it.

        Arguments
        - showing: whether the bedrock slate should be shown
        """
        ...


    def getBeamTarget(self) -> "Location":
        """
        Gets the location that this end crystal is pointing its beam to.

        Returns
        - the location that the beam is pointed to, or null if the beam is not shown
        """
        ...


    def setBeamTarget(self, location: "Location") -> None:
        """
        Sets the location that this end crystal is pointing to. Passing a null
        value will remove the current beam.

        Arguments
        - location: the location to point the beam to

        Raises
        - IllegalArgumentException: for differing worlds
        """
        ...
