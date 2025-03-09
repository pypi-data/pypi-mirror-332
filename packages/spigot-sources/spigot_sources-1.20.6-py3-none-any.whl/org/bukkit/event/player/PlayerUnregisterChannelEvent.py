"""
Python module generated from Java source file org.bukkit.event.player.PlayerUnregisterChannelEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerUnregisterChannelEvent(PlayerChannelEvent):
    """
    This is called immediately after a player unregisters for a plugin channel.
    """

    def __init__(self, player: "Player", channel: str):
        ...
