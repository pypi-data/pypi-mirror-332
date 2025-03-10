"""
Python module generated from Java source file org.bukkit.event.entity.PiglinBarterEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Piglin
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PiglinBarterEvent(EntityEvent, Cancellable):
    """
    Stores all data related to the bartering interaction with a piglin.
    
    This event can be triggered by a piglin picking up an item that's on its
    bartering list.
    """

    def __init__(self, what: "Piglin", input: "ItemStack", outcome: list["ItemStack"]):
        ...


    def getEntity(self) -> "Piglin":
        ...


    def getInput(self) -> "ItemStack":
        """
        Gets the input of the barter.

        Returns
        - The item that was used to barter with
        """
        ...


    def getOutcome(self) -> list["ItemStack"]:
        """
        Returns a mutable list representing the outcome of the barter.

        Returns
        - A mutable list of the item the player will receive
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
