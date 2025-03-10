"""
Python module generated from Java source file org.bukkit.event.block.BellRingEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BellRingEvent(BlockEvent, Cancellable):
    """
    Called when a bell is being rung.
    """

    def __init__(self, theBlock: "Block", direction: "BlockFace", entity: "Entity"):
        ...


    def getDirection(self) -> "BlockFace":
        """
        Get the direction in which the bell was rung.

        Returns
        - the direction
        """
        ...


    def getEntity(self) -> "Entity":
        """
        Get the Entity that rang the bell (if there was one).

        Returns
        - the entity
        """
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
