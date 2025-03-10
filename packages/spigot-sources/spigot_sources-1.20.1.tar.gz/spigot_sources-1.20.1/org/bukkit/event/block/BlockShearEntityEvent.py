"""
Python module generated from Java source file org.bukkit.event.block.BlockShearEntityEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockShearEntityEvent(BlockEvent, Cancellable):
    """
    Event fired when a dispenser shears a nearby sheep.
    """

    def __init__(self, dispenser: "Block", sheared: "Entity", tool: "ItemStack"):
        ...


    def getEntity(self) -> "Entity":
        """
        Gets the entity that was sheared.

        Returns
        - the entity that was sheared.
        """
        ...


    def getTool(self) -> "ItemStack":
        """
        Gets the item used to shear this sheep.

        Returns
        - the item used to shear this sheep.
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
