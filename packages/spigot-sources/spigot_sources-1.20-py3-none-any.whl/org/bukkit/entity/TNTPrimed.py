"""
Python module generated from Java source file org.bukkit.entity.TNTPrimed

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class TNTPrimed(Explosive):
    """
    Represents a Primed TNT.
    """

    def setFuseTicks(self, fuseTicks: int) -> None:
        """
        Set the number of ticks until the TNT blows up after being primed.

        Arguments
        - fuseTicks: The fuse ticks
        """
        ...


    def getFuseTicks(self) -> int:
        """
        Retrieve the number of ticks until the explosion of this TNTPrimed
        entity

        Returns
        - the number of ticks until this TNTPrimed explodes
        """
        ...


    def getSource(self) -> "Entity":
        """
        Gets the source of this primed TNT. The source is the entity
        responsible for the creation of this primed TNT. (I.E. player ignites
        TNT with flint and steel.) Take note that this can be null if there is
        no suitable source. (created by the org.bukkit.World.spawn(Location, Class) method, for example.)
        
        The source will become null if the chunk this primed TNT is in is
        unloaded then reloaded. The source entity may be invalid if for example
        it has since died or been unloaded. Callers should check
        Entity.isValid().

        Returns
        - the source of this primed TNT
        """
        ...


    def setSource(self, source: "Entity") -> None:
        """
        Sets the source of this primed TNT.
        
        The source is the entity responsible for the creation of this primed TNT.
        
        Must be instance of org.bukkit.entity.LivingEntity otherwise will
        be set to null. The parameter is typed org.bukkit.entity.Entity to be consistent with org.bukkit.entity.TNTPrimed.getSource() method.

        Arguments
        - source: the source of this primed TNT
        """
        ...
