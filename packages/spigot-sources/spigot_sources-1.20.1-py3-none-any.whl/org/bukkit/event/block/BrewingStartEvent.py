"""
Python module generated from Java source file org.bukkit.event.block.BrewingStartEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BrewingStartEvent(InventoryBlockStartEvent):
    """
    Called when a brewing stand starts to brew.
    """

    def __init__(self, furnace: "Block", source: "ItemStack", brewingTime: int):
        ...


    def getTotalBrewTime(self) -> int:
        """
        Gets the total brew time associated with this event.

        Returns
        - the total brew time
        """
        ...


    def setTotalBrewTime(self, brewTime: int) -> None:
        """
        Sets the total brew time for this event.

        Arguments
        - brewTime: the new total brew time
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
