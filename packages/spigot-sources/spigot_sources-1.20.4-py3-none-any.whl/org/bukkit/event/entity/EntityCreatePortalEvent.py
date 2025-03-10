"""
Python module generated from Java source file org.bukkit.event.entity.EntityCreatePortalEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import PortalType
from org.bukkit.block import BlockState
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.event.world import PortalCreateEvent
from typing import Any, Callable, Iterable, Tuple


class EntityCreatePortalEvent(EntityEvent, Cancellable):
    """
    Thrown when a Living Entity creates a portal in a world.

    Deprecated
    - Use PortalCreateEvent
    """

    def __init__(self, what: "LivingEntity", blocks: list["BlockState"], type: "PortalType"):
        ...


    def getEntity(self) -> "LivingEntity":
        ...


    def getBlocks(self) -> list["BlockState"]:
        """
        Gets a list of all blocks associated with the portal.

        Returns
        - List of blocks that will be changed.
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getPortalType(self) -> "PortalType":
        """
        Gets the type of portal that is trying to be created.

        Returns
        - Type of portal.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
