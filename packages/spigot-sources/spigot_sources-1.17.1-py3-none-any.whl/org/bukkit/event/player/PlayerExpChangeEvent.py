"""
Python module generated from Java source file org.bukkit.event.player.PlayerExpChangeEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerExpChangeEvent(PlayerEvent):
    """
    Called when a players experience changes naturally
    """

    def __init__(self, player: "Player", expAmount: int):
        ...


    def getAmount(self) -> int:
        """
        Get the amount of experience the player will receive

        Returns
        - The amount of experience
        """
        ...


    def setAmount(self, amount: int) -> None:
        """
        Set the amount of experience the player will receive

        Arguments
        - amount: The amount of experience to set
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
