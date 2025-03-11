"""
Python module generated from Java source file org.bukkit.entity.Creaking

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Creaking(Monster):
    """
    Represents a Creaking.
    """

    def getHome(self) -> "Location":
        """
        Gets the home location for this Creaking (ie where its corresponding
        org.bukkit.block.CreakingHeart can be).

        Returns
        - the location of the home.
        """
        ...


    def setHome(self, location: "Location") -> None:
        """
        Sets the home location for this Creaking.

        Arguments
        - location: the location of the home.
        """
        ...


    def activate(self, player: "Player") -> None:
        """
        Activate this Creaking to target and follow a player.

        Arguments
        - player: the target.
        """
        ...


    def deactivate(self) -> None:
        """
        Deactivate this Creaking from the current target player.
        """
        ...


    def isActive(self) -> bool:
        """
        Gets if this Creaking is active.

        Returns
        - True if is active.
        """
        ...
