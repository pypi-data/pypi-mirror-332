"""
Python module generated from Java source file org.bukkit.event.player.PlayerEditBookEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Bukkit
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory.meta import BookMeta
from typing import Any, Callable, Iterable, Tuple


class PlayerEditBookEvent(PlayerEvent, Cancellable):
    """
    Called when a player edits or signs a book and quill item. If the event is
    cancelled, no changes are made to the BookMeta
    """

    def __init__(self, who: "Player", slot: int, previousBookMeta: "BookMeta", newBookMeta: "BookMeta", isSigning: bool):
        ...


    def getPreviousBookMeta(self) -> "BookMeta":
        """
        Gets the book meta currently on the book.
        
        Note: this is a copy of the book meta. You cannot use this object to
        change the existing book meta.

        Returns
        - the book meta currently on the book
        """
        ...


    def getNewBookMeta(self) -> "BookMeta":
        """
        Gets the book meta that the player is attempting to add to the book.
        
        Note: this is a copy of the proposed new book meta. Use .setNewBookMeta(BookMeta) to change what will actually be added to the
        book.

        Returns
        - the book meta that the player is attempting to add
        """
        ...


    def getSlot(self) -> int:
        """
        Gets the inventory slot number for the book item that triggered this
        event.
        
        This is a slot number on the player's hotbar in the range 0-8, or -1 for
        off hand.

        Returns
        - the inventory slot number that the book item occupies

        Deprecated
        - books may be signed from off hand
        """
        ...


    def setNewBookMeta(self, newBookMeta: "BookMeta") -> None:
        """
        Sets the book meta that will actually be added to the book.

        Arguments
        - newBookMeta: new book meta

        Raises
        - IllegalArgumentException: if the new book meta is null
        """
        ...


    def isSigning(self) -> bool:
        """
        Gets whether or not the book is being signed. If a book is signed the
        Material changes from BOOK_AND_QUILL to WRITTEN_BOOK.

        Returns
        - True if the book is being signed
        """
        ...


    def setSigning(self, signing: bool) -> None:
        """
        Sets whether or not the book is being signed. If a book is signed the
        Material changes from BOOK_AND_QUILL to WRITTEN_BOOK.

        Arguments
        - signing: whether or not the book is being signed.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
