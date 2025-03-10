"""
Python module generated from Java source file org.bukkit.event.entity.SheepRegrowWoolEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Sheep
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class SheepRegrowWoolEvent(EntityEvent, Cancellable):
    """
    Called when a sheep regrows its wool
    """

    def __init__(self, sheep: "Sheep"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Sheep":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
