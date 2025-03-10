"""
Python module generated from Java source file org.bukkit.event.inventory.BrewEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

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
from typing import Any, Callable, Iterable, Tuple


class BrewEvent(BlockEvent, Cancellable):
    """
    Called when the brewing of the contents inside the Brewing Stand is
    complete.
    """

    def __init__(self, brewer: "Block", contents: "BrewerInventory", fuelLevel: int):
        ...


    def getContents(self) -> "BrewerInventory":
        """
        Gets the contents of the Brewing Stand.

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


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
