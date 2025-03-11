"""
Python module generated from Java source file org.bukkit.event.player.PlayerSpawnChangeEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import Location
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerSpawnChangeEvent(PlayerEvent, Cancellable):
    """
    This event is fired when the spawn point of the player is changed.

    Unknown Tags
    - draft API
    """

    def __init__(self, player: "Player", newSpawn: "Location", forced: bool, cause: "Cause"):
        ...


    def getCause(self) -> "Cause":
        """
        Gets the cause of spawn change.

        Returns
        - change cause
        """
        ...


    def isForced(self) -> bool:
        """
        Gets if the spawn position will be used regardless of bed obstruction
        rules.

        Returns
        - True if is forced
        """
        ...


    def setForced(self, forced: bool) -> None:
        """
        Sets if the spawn position will be used regardless of bed obstruction
        rules.

        Arguments
        - forced: True if forced
        """
        ...


    def getNewSpawn(self) -> "Location":
        """
        Gets the new spawn to be set.

        Returns
        - new spawn location
        """
        ...


    def setNewSpawn(self, newSpawn: "Location") -> None:
        """
        Sets the new spawn location.

        Arguments
        - newSpawn: new spawn location, with non-null world
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


    class Cause(Enum):

        COMMAND = 0
        """
        Indicate the spawn was set by a command.
        """
        BED = 1
        """
        Indicate the spawn was set by the player interacting with a bed.
        """
        RESPAWN_ANCHOR = 2
        """
        Indicate the spawn was set by the player interacting with a respawn
        anchor.
        """
        PLUGIN = 3
        """
        Indicate the spawn was set by the use of plugins.
        """
        RESET = 4
        """
        Indicate the spawn was reset by an invalid bed position or empty
        respawn anchor.
        """
        UNKNOWN = 5
        """
        Indicate the spawn was caused by an unknown reason.
        """
