"""
Python module generated from Java source file org.bukkit.event.server.BroadcastMessageEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import AsyncPlayerChatEvent
from org.bukkit.event.server import *
from typing import Any, Callable, Iterable, Tuple


class BroadcastMessageEvent(ServerEvent, Cancellable):
    """
    Event triggered for server broadcast messages such as from
    org.bukkit.Server.broadcast(String, String).
    
    **This event behaves similarly to AsyncPlayerChatEvent in that it
    should be async if fired from an async thread. Please see that event for
    further information.**
    """

    def __init__(self, message: str, recipients: set["CommandSender"]):
        ...


    def __init__(self, isAsync: bool, message: str, recipients: set["CommandSender"]):
        ...


    def getMessage(self) -> str:
        """
        Get the message to broadcast.

        Returns
        - Message to broadcast
        """
        ...


    def setMessage(self, message: str) -> None:
        """
        Set the message to broadcast.

        Arguments
        - message: New message to broadcast
        """
        ...


    def getRecipients(self) -> set["CommandSender"]:
        """
        Gets a set of recipients that this chat message will be displayed to.
        
        The set returned is not guaranteed to be mutable and may auto-populate
        on access. Any listener accessing the returned set should be aware that
        it may reduce performance for a lazy set implementation.
        
        Listeners should be aware that modifying the list may throw UnsupportedOperationException if the event caller provides an
        unmodifiable set.

        Returns
        - All CommandSenders who will see this chat message
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
