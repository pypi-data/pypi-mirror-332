"""
Python module generated from Java source file org.bukkit.event.block.InventoryBlockStartEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.event.inventory import FurnaceStartSmeltEvent
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class InventoryBlockStartEvent(BlockEvent):
    """
    Used when:
    
    - A Furnace starts smelting FurnaceStartSmeltEvent
    - A Brewing-Stand starts brewing BrewingStartEvent
    - A Campfire starts cooking CampfireStartEvent

    Unknown Tags
    - draft API
    """

    def __init__(self, block: "Block", source: "ItemStack"):
        ...


    def getSource(self) -> "ItemStack":
        """
        Gets the source ItemStack for this event.

        Returns
        - the source ItemStack
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
