"""
Python module generated from Java source file org.bukkit.event.player.PlayerAnimationEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerAnimationEvent(PlayerEvent, Cancellable):
    """
    Represents a player animation event
    """

    def __init__(self, player: "Player"):
        ...


    def __init__(self, player: "Player", playerAnimationType: "PlayerAnimationType"):
        """
        Construct a new PlayerAnimation event

        Arguments
        - player: The player instance
        - playerAnimationType: The animation type
        """
        ...


    def getAnimationType(self) -> "PlayerAnimationType":
        """
        Get the type of this animation event

        Returns
        - the animation type
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
