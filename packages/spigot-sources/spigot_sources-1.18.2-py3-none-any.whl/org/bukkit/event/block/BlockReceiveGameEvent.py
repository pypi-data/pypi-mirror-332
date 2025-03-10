"""
Python module generated from Java source file org.bukkit.event.block.BlockReceiveGameEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GameEvent
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockReceiveGameEvent(BlockEvent, Cancellable):
    """
    Called when a Sculk sensor receives a game event and hence might activate.
    
    Will be called cancelled if the block's default behavior is to ignore the
    event.
    """

    def __init__(self, event: "GameEvent", block: "Block", entity: "Entity"):
        ...


    def getEvent(self) -> "GameEvent":
        """
        Get the underlying event.

        Returns
        - the event
        """
        ...


    def getEntity(self) -> "Entity":
        """
        Get the entity which triggered this event, if present.

        Returns
        - triggering entity or null
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
