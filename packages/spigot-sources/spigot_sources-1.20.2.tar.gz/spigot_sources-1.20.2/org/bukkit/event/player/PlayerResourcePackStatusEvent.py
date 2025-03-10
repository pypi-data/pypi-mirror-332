"""
Python module generated from Java source file org.bukkit.event.player.PlayerResourcePackStatusEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerResourcePackStatusEvent(PlayerEvent):
    """
    Called when a player takes action on a resource pack request sent via
    Player.setResourcePack(java.lang.String).
    """

    def __init__(self, who: "Player", resourcePackStatus: "Status"):
        ...


    def getStatus(self) -> "Status":
        """
        Gets the status of this pack.

        Returns
        - the current status
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Status(Enum):
        """
        Status of the resource pack.
        """

        SUCCESSFULLY_LOADED = 0
        """
        The resource pack has been successfully downloaded and applied to the
        client.
        """
        DECLINED = 1
        """
        The client refused to accept the resource pack.
        """
        FAILED_DOWNLOAD = 2
        """
        The client accepted the pack, but download failed.
        """
        ACCEPTED = 3
        """
        The client accepted the pack and is beginning a download of it.
        """
