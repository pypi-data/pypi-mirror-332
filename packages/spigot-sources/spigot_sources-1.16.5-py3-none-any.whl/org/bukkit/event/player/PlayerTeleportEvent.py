"""
Python module generated from Java source file org.bukkit.event.player.PlayerTeleportEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Location
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerTeleportEvent(PlayerMoveEvent):
    """
    Holds information for player teleport events
    """

    def __init__(self, player: "Player", from: "Location", to: "Location"):
        ...


    def __init__(self, player: "Player", from: "Location", to: "Location", cause: "TeleportCause"):
        ...


    def getCause(self) -> "TeleportCause":
        """
        Gets the cause of this teleportation event

        Returns
        - Cause of the event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class TeleportCause(Enum):

        ENDER_PEARL = 0
        """
        Indicates the teleporation was caused by a player throwing an Ender
        Pearl
        """
        COMMAND = 1
        """
        Indicates the teleportation was caused by a player executing a
        command
        """
        PLUGIN = 2
        """
        Indicates the teleportation was caused by a plugin
        """
        NETHER_PORTAL = 3
        """
        Indicates the teleportation was caused by a player entering a
        Nether portal
        """
        END_PORTAL = 4
        """
        Indicates the teleportation was caused by a player entering an End
        portal
        """
        SPECTATE = 5
        """
        Indicates the teleportation was caused by a player teleporting to a
        Entity/Player via the spectator menu
        """
        END_GATEWAY = 6
        """
        Indicates the teleportation was caused by a player entering an End
        gateway
        """
        CHORUS_FRUIT = 7
        """
        Indicates the teleportation was caused by a player consuming chorus
        fruit
        """
        UNKNOWN = 8
        """
        Indicates the teleportation was caused by an event not covered by
        this enum
        """
