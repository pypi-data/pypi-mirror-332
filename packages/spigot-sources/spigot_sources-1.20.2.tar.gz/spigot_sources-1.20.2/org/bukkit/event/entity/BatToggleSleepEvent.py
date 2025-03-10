"""
Python module generated from Java source file org.bukkit.event.entity.BatToggleSleepEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Bat
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class BatToggleSleepEvent(EntityEvent, Cancellable):
    """
    Called when a bat attempts to sleep or wake up from its slumber.
    
    If a Bat Toggle Sleep event is cancelled, the Bat will not toggle its sleep
    state.
    """

    def __init__(self, what: "Bat", awake: bool):
        ...


    def isAwake(self) -> bool:
        """
        Get whether or not the bat is attempting to awaken.

        Returns
        - True if trying to awaken, False otherwise
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
