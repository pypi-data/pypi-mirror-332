"""
Python module generated from Java source file org.bukkit.event.entity.FireworkExplodeEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Firework
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class FireworkExplodeEvent(EntityEvent, Cancellable):
    """
    Called when a firework explodes.
    """

    def __init__(self, what: "Firework"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Set the cancelled state of this event. If the firework explosion is
        cancelled, the firework will still be removed, but no particles will be
        displayed.

        Arguments
        - cancel: whether to cancel or not.
        """
        ...


    def getEntity(self) -> "Firework":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
