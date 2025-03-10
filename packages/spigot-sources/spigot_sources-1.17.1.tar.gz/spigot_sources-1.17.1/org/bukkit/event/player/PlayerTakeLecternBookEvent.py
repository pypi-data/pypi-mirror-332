"""
Python module generated from Java source file org.bukkit.event.player.PlayerTakeLecternBookEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Lectern
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerTakeLecternBookEvent(PlayerEvent, Cancellable):
    """
    This event is called when a player clicks the button to take a book of a
    Lectern. If this event is cancelled the book remains on the lectern.
    """

    def __init__(self, who: "Player", lectern: "Lectern"):
        ...


    def getLectern(self) -> "Lectern":
        """
        Gets the lectern involved.

        Returns
        - the Lectern
        """
        ...


    def getBook(self) -> "ItemStack":
        """
        Gets the current ItemStack on the lectern.

        Returns
        - the ItemStack on the Lectern
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
