"""
Python module generated from Java source file org.bukkit.event.world.TimeSkipEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import World
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.world import *
from typing import Any, Callable, Iterable, Tuple


class TimeSkipEvent(WorldEvent, Cancellable):
    """
    Called when the time skips in a world.
    
    If the event is cancelled the time will not change.
    """

    def __init__(self, world: "World", skipReason: "SkipReason", skipAmount: int):
        ...


    def getSkipReason(self) -> "SkipReason":
        """
        Gets the reason why the time has skipped.

        Returns
        - a SkipReason value detailing why the time has skipped
        """
        ...


    def getSkipAmount(self) -> int:
        """
        Gets the amount of time that was skipped.

        Returns
        - Amount of time skipped
        """
        ...


    def setSkipAmount(self, skipAmount: int) -> None:
        """
        Sets the amount of time to skip.

        Arguments
        - skipAmount: Amount of time to skip
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


    class SkipReason(Enum):
        """
        An enum specifying the reason the time skipped.
        """

        COMMAND = 0
        """
        When time is changed using the vanilla /time command.
        """
        CUSTOM = 1
        """
        When time is changed by a plugin.
        """
        NIGHT_SKIP = 2
        """
        When time is changed by all players sleeping in their beds and the
        night skips.
        """
