"""
Python module generated from Java source file org.bukkit.event.player.AsyncPlayerChatEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import IllegalFormatException
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class AsyncPlayerChatEvent(PlayerEvent, Cancellable):
    """
    This event will sometimes fire synchronously, depending on how it was
    triggered.
    
    The constructor provides a boolean to indicate if the event was fired
    synchronously or asynchronously. When asynchronous, this event can be
    called from any thread, sans the main thread, and has limited access to the
    API.
    
    If a player is the direct cause of this event by an incoming packet, this
    event will be asynchronous. If a plugin triggers this event by compelling a
    player to chat, this event will be synchronous.
    
    Care should be taken to check .isAsynchronous() and treat the event
    appropriately.
    """

    def __init__(self, async: bool, who: "Player", message: str, players: set["Player"]):
        """
        Arguments
        - async: This changes the event to a synchronous state.
        - who: the chat sender
        - message: the message sent
        - players: the players to receive the message. This may be a lazy
            or unmodifiable collection.
        """
        ...


    def getMessage(self) -> str:
        """
        Gets the message that the player is attempting to send. This message
        will be used with .getFormat().

        Returns
        - Message the player is attempting to send
        """
        ...


    def setMessage(self, message: str) -> None:
        """
        Sets the message that the player will send. This message will be used
        with .getFormat().

        Arguments
        - message: New message that the player will send
        """
        ...


    def getFormat(self) -> str:
        """
        Gets the format to use to display this chat message.
        
        When this event finishes execution, the first format parameter is the
        Player.getDisplayName() and the second parameter is .getMessage()

        Returns
        - String.format(String, Object...) compatible format
            string
        """
        ...


    def setFormat(self, format: str) -> None:
        """
        Sets the format to use to display this chat message.
        
        When this event finishes execution, the first format parameter is the
        Player.getDisplayName() and the second parameter is .getMessage()

        Arguments
        - format: String.format(String, Object...) compatible
            format string

        Raises
        - IllegalFormatException: if the underlying API throws the
            exception
        - NullPointerException: if format is null

        See
        - String.format(String, Object...)
        """
        ...


    def getRecipients(self) -> set["Player"]:
        """
        Gets a set of recipients that this chat message will be displayed to.
        
        The set returned is not guaranteed to be mutable and may auto-populate
        on access. Any listener accessing the returned set should be aware that
        it may reduce performance for a lazy set implementation.
        
        Listeners should be aware that modifying the list may throw UnsupportedOperationException if the event caller provides an
        unmodifiable set.

        Returns
        - All Players who will see this chat message
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
