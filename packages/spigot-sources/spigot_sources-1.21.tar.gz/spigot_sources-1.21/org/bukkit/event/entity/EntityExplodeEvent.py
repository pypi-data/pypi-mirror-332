"""
Python module generated from Java source file org.bukkit.event.entity.EntityExplodeEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ExplosionResult
from org.bukkit import Location
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityExplodeEvent(EntityEvent, Cancellable):
    """
    Called when an entity explodes
    """

    def __init__(self, what: "Entity", location: "Location", blocks: list["Block"], yield: float, result: "ExplosionResult"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getExplosionResult(self) -> "ExplosionResult":
        """
        Returns the result of the explosion if it is not cancelled.

        Returns
        - the result of the explosion
        """
        ...


    def blockList(self) -> list["Block"]:
        """
        Returns the list of blocks that would have been removed or were removed
        from the explosion event.

        Returns
        - All blown-up blocks
        """
        ...


    def getLocation(self) -> "Location":
        """
        Returns the location where the explosion happened.
        
        It is not possible to get this value from the Entity as the Entity no
        longer exists in the world.

        Returns
        - The location of the explosion
        """
        ...


    def getYield(self) -> float:
        """
        Returns the percentage of blocks to drop from this explosion

        Returns
        - The yield.
        """
        ...


    def setYield(self, yield: float) -> None:
        """
        Sets the percentage of blocks to drop from this explosion

        Arguments
        - yield: The new yield percentage
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
