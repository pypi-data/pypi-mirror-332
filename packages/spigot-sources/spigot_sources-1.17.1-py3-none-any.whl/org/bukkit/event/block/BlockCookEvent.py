"""
Python module generated from Java source file org.bukkit.event.block.BlockCookEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockCookEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is successfully cooked in a block.
    """

    def __init__(self, block: "Block", source: "ItemStack", result: "ItemStack"):
        ...


    def getSource(self) -> "ItemStack":
        """
        Gets the smelted ItemStack for this event

        Returns
        - smelting source ItemStack
        """
        ...


    def getResult(self) -> "ItemStack":
        """
        Gets the resultant ItemStack for this event

        Returns
        - smelting result ItemStack
        """
        ...


    def setResult(self, result: "ItemStack") -> None:
        """
        Sets the resultant ItemStack for this event

        Arguments
        - result: new result ItemStack
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
