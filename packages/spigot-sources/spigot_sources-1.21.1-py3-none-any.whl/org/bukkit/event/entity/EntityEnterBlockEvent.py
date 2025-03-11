"""
Python module generated from Java source file org.bukkit.event.entity.EntityEnterBlockEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

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


class EntityEnterBlockEvent(EntityEvent, Cancellable):
    """
    Called when an Entity enters a block and is stored in that block.
    
    This event is called for bees entering a bee hive.
    
    It is not called when a silverfish "enters" a stone block. For that listen to
    the EntityChangeBlockEvent.
    """

    def __init__(self, entity: "Entity", block: "Block"):
        ...


    def getBlock(self) -> "Block":
        """
        Get the block the entity will enter.

        Returns
        - the block
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
