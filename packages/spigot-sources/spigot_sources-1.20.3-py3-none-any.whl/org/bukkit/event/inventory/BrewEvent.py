"""
Python module generated from Java source file org.bukkit.event.inventory.BrewEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.event.inventory import *
from org.bukkit.inventory import BrewerInventory
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BrewEvent(BlockEvent, Cancellable):
    """
    Called when the brewing of the contents inside the Brewing Stand is
    complete.
    """

    def __init__(self, brewer: "Block", contents: "BrewerInventory", results: list["ItemStack"], fuelLevel: int):
        ...


    def getContents(self) -> "BrewerInventory":
        """
        Gets the contents of the Brewing Stand.
        
        **Note:** The brewer inventory still holds the items found prior to
        the finalization of the brewing process, e.g. the plain water bottles.

        Returns
        - the contents
        """
        ...


    def getFuelLevel(self) -> int:
        """
        Gets the remaining fuel level.

        Returns
        - the remaining fuel
        """
        ...


    def getResults(self) -> list["ItemStack"]:
        """
        Gets the resulting items in the Brewing Stand.
        
        The returned list, in case of a server-created event instance, is
        mutable. Any changes in the returned list will reflect in the brewing
        result if the event is not cancelled. If the size of the list is reduced,
        remaining items will be set to air.

        Returns
        - List of ItemStack resulting for this operation
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
