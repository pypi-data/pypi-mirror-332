"""
Python module generated from Java source file org.bukkit.event.entity.StriderTemperatureChangeEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Strider
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class StriderTemperatureChangeEvent(EntityEvent):
    """
    Called when a Strider's temperature has changed as a result of
    entering or existing blocks it considers warm.
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


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
