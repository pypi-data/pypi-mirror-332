"""
Python module generated from Java source file org.bukkit.event.player.PlayerExpCooldownChangeEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerExpCooldownChangeEvent(PlayerEvent):
    """
    Called when a player's experience cooldown changes.
    """

    def __init__(self, player: "Player", newcooldown: int, reason: "ChangeReason"):
        ...


    def getReason(self) -> "ChangeReason":
        """
        Gets the reason for the change.

        Returns
        - The reason for the change
        """
        ...


    def getNewCooldown(self) -> int:
        """
        Gets the new cooldown for the player.

        Returns
        - The new cooldown

        See
        - Player.getExpCooldown()
        """
        ...


    def setNewCooldown(self, newCooldown: int) -> None:
        """
        Sets the new cooldown for the player.

        Arguments
        - newCooldown: The new cooldown to set

        See
        - Player.setExpCooldown(int)
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class ChangeReason(Enum):

        PICKUP_ORB = 0
        """
        The cooldown was set by picking up an experience orb.
        """
        PLUGIN = 1
        """
        The cooldown was set by a plugin.

        See
        - Player.setExpCooldown(int)
        """
