"""
Python module generated from Java source file org.bukkit.event.raid.RaidStopEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.event import HandlerList
from org.bukkit.event.raid import *
from typing import Any, Callable, Iterable, Tuple


class RaidStopEvent(RaidEvent):
    """
    Called when a Raid is stopped.
    """

    def __init__(self, raid: "Raid", world: "World", reason: "Reason"):
        ...


    def getReason(self) -> "Reason":
        """
        Returns the stop reason.

        Returns
        - Reason
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Reason(Enum):

        PEACE = 0
        """
        Because the difficulty has been changed to peaceful.
        """
        TIMEOUT = 1
        """
        The raid took a long time without a final result.
        """
        FINISHED = 2
        """
        Finished the raid.
        """
        UNSPAWNABLE = 3
        """
        Couldn't find a suitable place to spawn raiders.
        """
        NOT_IN_VILLAGE = 4
        """
        The place where the raid occurs no longer be a village.
        """
