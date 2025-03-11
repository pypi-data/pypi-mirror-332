"""
Python module generated from Java source file org.bukkit.event.player.PlayerChannelEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerChannelEvent(PlayerEvent):
    """
    This event is called after a player registers or unregisters a new plugin
    channel.
    """

    def __init__(self, player: "Player", channel: str):
        ...


    def getChannel(self) -> str:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
