"""
Python module generated from Java source file org.bukkit.event.inventory.FurnaceBurnEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.event.inventory import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class FurnaceBurnEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is successfully burned as fuel in a furnace.
    """

    def __init__(self, furnace: "Block", fuel: "ItemStack", burnTime: int):
        ...


    def getFuel(self) -> "ItemStack":
        """
        Gets the fuel ItemStack for this event

        Returns
        - the fuel ItemStack
        """
        ...


    def getBurnTime(self) -> int:
        """
        Gets the burn time for this fuel

        Returns
        - the burn time for this fuel
        """
        ...


    def setBurnTime(self, burnTime: int) -> None:
        """
        Sets the burn time for this fuel

        Arguments
        - burnTime: the burn time for this fuel
        """
        ...


    def isBurning(self) -> bool:
        """
        Gets whether the furnace's fuel is burning or not.

        Returns
        - whether the furnace's fuel is burning or not.
        """
        ...


    def setBurning(self, burning: bool) -> None:
        """
        Sets whether the furnace's fuel is burning or not.

        Arguments
        - burning: True if the furnace's fuel is burning
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
