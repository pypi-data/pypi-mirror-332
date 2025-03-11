"""
Python module generated from Java source file org.bukkit.event.world.PortalCreateEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import World
from org.bukkit.block import BlockState
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class PortalCreateEvent(WorldEvent, Cancellable):
    """
    Called when a portal is created
    """

    def __init__(self, blocks: list["BlockState"], world: "World", reason: "CreateReason"):
        ...


    def __init__(self, blocks: list["BlockState"], world: "World", entity: "Entity", reason: "CreateReason"):
        ...


    def getBlocks(self) -> list["BlockState"]:
        """
        Gets an array list of all the blocks associated with the created portal

        Returns
        - array list of all the blocks associated with the created portal
        """
        ...


    def getEntity(self) -> "Entity":
        """
        Returns the Entity that triggered this portal creation (if available)

        Returns
        - Entity involved in this event
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getReason(self) -> "CreateReason":
        """
        Gets the reason for the portal's creation

        Returns
        - CreateReason for the portal's creation
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class CreateReason(Enum):
        """
        An enum to specify the various reasons for a portal's creation
        """

        FIRE = 0
        """
        When the blocks inside a portal are created due to a portal frame
        being set on fire.
        """
        NETHER_PAIR = 1
        """
        When a nether portal frame and portal is created at the exit of an
        entered nether portal.
        """
        END_PLATFORM = 2
        """
        When the target end platform is created as a result of a player
        entering an end portal.
        """
