"""
Python module generated from Java source file org.bukkit.event.entity.StriderTemperatureChangeEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Strider
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class StriderTemperatureChangeEvent(EntityEvent, Cancellable):
    """
    Called when a Strider's temperature has changed as a result of
    entering or exiting blocks it considers warm.
    """

    def __init__(self, what: "Strider", shivering: bool):
        ...


    def getEntity(self) -> "Strider":
        ...


    def isShivering(self) -> bool:
        """
        Get the Strider's new shivering state.

        Returns
        - the new shivering state
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
