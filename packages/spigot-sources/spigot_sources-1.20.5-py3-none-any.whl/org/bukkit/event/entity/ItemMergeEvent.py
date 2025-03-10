"""
Python module generated from Java source file org.bukkit.event.entity.ItemMergeEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Item
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ItemMergeEvent(EntityEvent, Cancellable):

    def __init__(self, item: "Item", target: "Item"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getEntity(self) -> "Item":
        ...


    def getTarget(self) -> "Item":
        """
        Gets the Item entity the main Item is being merged into.

        Returns
        - The Item being merged with
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
