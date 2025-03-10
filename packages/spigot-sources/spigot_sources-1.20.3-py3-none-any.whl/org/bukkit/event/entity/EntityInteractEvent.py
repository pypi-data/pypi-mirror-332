"""
Python module generated from Java source file org.bukkit.event.entity.EntityInteractEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityInteractEvent(EntityEvent, Cancellable):
    """
    Called when an entity interacts with an object
    """

    def __init__(self, entity: "Entity", block: "Block"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getBlock(self) -> "Block":
        """
        Returns the involved block

        Returns
        - the block clicked with this item.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
