"""
Python module generated from Java source file org.bukkit.event.player.PlayerPickupArrowEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AbstractArrow
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerPickupArrowEvent(PlayerPickupItemEvent):
    """
    Thrown when a player picks up an arrow from the ground.
    """

    def __init__(self, player: "Player", item: "Item", arrow: "AbstractArrow"):
        ...


    def getArrow(self) -> "AbstractArrow":
        """
        Get the arrow being picked up by the player

        Returns
        - The arrow being picked up
        """
        ...
