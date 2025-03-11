"""
Python module generated from Java source file org.bukkit.event.block.SignChangeEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block.sign import Side
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class SignChangeEvent(BlockEvent, Cancellable):
    """
    Called when a sign is changed by a player.
    
    If a Sign Change event is cancelled, the sign will not be changed.
    """

    def __init__(self, theBlock: "Block", thePlayer: "Player", theLines: list[str]):
        ...


    def __init__(self, theBlock: "Block", thePlayer: "Player", theLines: list[str], side: "Side"):
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player changing the sign involved in this event.

        Returns
        - the Player involved in this event
        """
        ...


    def getLines(self) -> list[str]:
        """
        Gets all of the lines of text from the sign involved in this event.

        Returns
        - the String array for the sign's lines new text
        """
        ...


    def getLine(self, index: int) -> str:
        """
        Gets a single line of text from the sign involved in this event.

        Arguments
        - index: index of the line to get

        Returns
        - the String containing the line of text associated with the
            provided index

        Raises
        - IndexOutOfBoundsException: thrown when the provided index is > 3
            or < 0
        """
        ...


    def setLine(self, index: int, line: str) -> None:
        """
        Sets a single line for the sign involved in this event

        Arguments
        - index: index of the line to set
        - line: text to set

        Raises
        - IndexOutOfBoundsException: thrown when the provided index is > 3
            or < 0
        """
        ...


    def getSide(self) -> "Side":
        """
        Returns which side is changed.

        Returns
        - the affected side of the sign
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
