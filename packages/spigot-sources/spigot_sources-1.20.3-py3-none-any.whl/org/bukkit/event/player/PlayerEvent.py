"""
Python module generated from Java source file org.bukkit.event.player.PlayerEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Event
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerEvent(Event):
    """
    Represents a player related event
    """

    def __init__(self, who: "Player"):
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player involved in this event

        Returns
        - Player who is involved in this event
        """
        ...
