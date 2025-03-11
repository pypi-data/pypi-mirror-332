"""
Python module generated from Java source file org.bukkit.inventory.meta.CompassMeta

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class CompassMeta(ItemMeta):
    """
    Represents a compass that can track a specific location.
    """

    def hasLodestone(self) -> bool:
        """
        Checks if this compass has been paired to a lodestone.

        Returns
        - paired status
        """
        ...


    def getLodestone(self) -> "Location":
        """
        Gets the location that this compass will point to.
        
        Check .hasLodestone() first!

        Returns
        - lodestone location
        """
        ...


    def setLodestone(self, lodestone: "Location") -> None:
        """
        Sets the location this lodestone compass will point to.

        Arguments
        - lodestone: new location or null to clear
        """
        ...


    def isLodestoneTracked(self) -> bool:
        """
        Gets if this compass is tracking a specific lodestone.
        
        If True the compass will only work if there is a lodestone at the tracked
        location.

        Returns
        - lodestone tracked
        """
        ...


    def setLodestoneTracked(self, tracked: bool) -> None:
        """
        Sets if this compass is tracking a specific lodestone.
        
        If True the compass will only work if there is a lodestone at the tracked
        location.

        Arguments
        - tracked: new tracked status
        """
        ...


    def clone(self) -> "CompassMeta":
        ...
