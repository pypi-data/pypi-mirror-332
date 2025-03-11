"""
Python module generated from Java source file org.bukkit.event.entity.SlimeSplitEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Slime
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class SlimeSplitEvent(EntityEvent, Cancellable):
    """
    Called when a Slime splits into smaller Slimes upon death
    """

    def __init__(self, slime: "Slime", count: int):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Slime":
        ...


    def getCount(self) -> int:
        """
        Gets the amount of smaller slimes to spawn

        Returns
        - the amount of slimes to spawn
        """
        ...


    def setCount(self, count: int) -> None:
        """
        Sets how many smaller slimes will spawn on the split

        Arguments
        - count: the amount of slimes to spawn
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
