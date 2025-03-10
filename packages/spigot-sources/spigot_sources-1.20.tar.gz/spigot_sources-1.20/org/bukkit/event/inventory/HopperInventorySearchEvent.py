"""
Python module generated from Java source file org.bukkit.event.inventory.HopperInventorySearchEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Inventory
from typing import Any, Callable, Iterable, Tuple


class HopperInventorySearchEvent(BlockEvent):
    """
    Event that gets called each time a Hopper attempts to find its
    source/attached containers.
    """

    def __init__(self, inventory: "Inventory", containerType: "ContainerType", hopper: "Block", searchBlock: "Block"):
        ...


    def setInventory(self, inventory: "Inventory") -> None:
        """
        Set the Inventory that the Hopper will use for its
        source/attached Container.

        Arguments
        - inventory: the inventory to use
        """
        ...


    def getInventory(self) -> "Inventory":
        """
        Gets the Inventory that the Hopper will use for its
        source/attached Container.

        Returns
        - the inventory which will be used
        """
        ...


    def getContainerType(self) -> "ContainerType":
        """
        Gets the Container type the Hopper is searching for.

        Returns
        - the container type being searched for
        """
        ...


    def getSearchBlock(self) -> "Block":
        """
        Gets the Block that is being searched for an inventory.

        Returns
        - block being searched for an inventory
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class ContainerType(Enum):

        SOURCE = 0
        """
        The source container the hopper is looking for.
        
        This is the Inventory above the Hopper where it extracts items from.
        """
        DESTINATION = 1
        """
        The container the hopper is attached to.
        
        This is the Inventory the Hopper pushes items into.
        """
