"""
Python module generated from Java source file org.bukkit.event.inventory.BrewingStandFuelEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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


class BrewingStandFuelEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is about to increase the fuel level of a brewing
    stand.
    """

    def __init__(self, brewingStand: "Block", fuel: "ItemStack", fuelPower: int):
        ...


    def getFuel(self) -> "ItemStack":
        """
        Gets the ItemStack of the fuel before the amount was subtracted.

        Returns
        - the fuel ItemStack
        """
        ...


    def getFuelPower(self) -> int:
        """
        Gets the fuel power for this fuel. Each unit of power can fuel one
        brewing operation.

        Returns
        - the fuel power for this fuel
        """
        ...


    def setFuelPower(self, fuelPower: int) -> None:
        """
        Sets the fuel power for this fuel. Each unit of power can fuel one
        brewing operation.

        Arguments
        - fuelPower: the fuel power for this fuel
        """
        ...


    def isConsuming(self) -> bool:
        """
        Gets whether the brewing stand's fuel will be reduced / consumed or not.

        Returns
        - whether the fuel will be reduced or not
        """
        ...


    def setConsuming(self, consuming: bool) -> None:
        """
        Sets whether the brewing stand's fuel will be reduced / consumed or not.

        Arguments
        - consuming: whether the fuel will be reduced or not
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
