"""
Python module generated from Java source file org.bukkit.event.entity.SheepDyeWoolEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.entity import Player
from org.bukkit.entity import Sheep
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class SheepDyeWoolEvent(EntityEvent, Cancellable):
    """
    Called when a sheep's wool is dyed
    """

    def __init__(self, sheep: "Sheep", color: "DyeColor"):
        ...


    def __init__(self, sheep: "Sheep", color: "DyeColor", player: "Player"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Sheep":
        ...


    def getPlayer(self) -> "Player":
        """
        Returns the player dyeing the sheep, if available.

        Returns
        - player or null
        """
        ...


    def getColor(self) -> "DyeColor":
        """
        Gets the DyeColor the sheep is being dyed

        Returns
        - the DyeColor the sheep is being dyed
        """
        ...


    def setColor(self, color: "DyeColor") -> None:
        """
        Sets the DyeColor the sheep is being dyed

        Arguments
        - color: the DyeColor the sheep will be dyed
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
