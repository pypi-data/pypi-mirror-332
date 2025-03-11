"""
Python module generated from Java source file org.bukkit.event.player.PlayerInputEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Input
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerInputEvent(PlayerEvent):
    """
    This event is called when a player sends updated input to the server.

    See
    - Player.getCurrentInput()
    """

    def __init__(self, player: "Player", input: "Input"):
        ...


    def getInput(self) -> "Input":
        """
        Gets the new input received from this player.

        Returns
        - the new input
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
