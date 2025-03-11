"""
Python module generated from Java source file org.bukkit.event.entity.EntityChangeBlockEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityChangeBlockEvent(EntityEvent, Cancellable):
    """
    Called when any Entity changes a block and a more specific event is not available.
    """

    def __init__(self, what: "Entity", block: "Block", to: "BlockData"):
        ...


    def getBlock(self) -> "Block":
        """
        Gets the block the entity is changing

        Returns
        - the block that is changing
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getTo(self) -> "Material":
        """
        Gets the Material that the block is changing into

        Returns
        - the material that the block is changing into
        """
        ...


    def getBlockData(self) -> "BlockData":
        """
        Gets the data for the block that would be changed into

        Returns
        - the data for the block that would be changed into
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
