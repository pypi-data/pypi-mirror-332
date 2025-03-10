"""
Python module generated from Java source file org.bukkit.event.player.PlayerChatEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Warning
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerChatEvent(PlayerEvent, Cancellable):
    """
    Holds information for player chat and commands

    Deprecated
    - This event will fire from the main thread and allows the use of
        all of the Bukkit API, unlike the AsyncPlayerChatEvent.
        
        Listening to this event forces chat to wait for the main thread which
        causes delays for chat. AsyncPlayerChatEvent is the encouraged
        alternative for thread safe implementations.
    """

    def __init__(self, player: "Player", message: str):
        ...


    def __init__(self, player: "Player", message: str, format: str, recipients: set["Player"]):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getMessage(self) -> str:
        """
        Gets the message that the player is attempting to send

        Returns
        - Message the player is attempting to send
        """
        ...


    def setMessage(self, message: str) -> None:
        """
        Sets the message that the player will send

        Arguments
        - message: New message that the player will send
        """
        ...


    def setPlayer(self, player: "Player") -> None:
        """
        Sets the player that this message will display as, or command will be
        executed as

        Arguments
        - player: New player which this event will execute as
        """
        ...


    def getFormat(self) -> str:
        """
        Gets the format to use to display this chat message

        Returns
        - String.Format compatible format string
        """
        ...


    def setFormat(self, format: str) -> None:
        """
        Sets the format to use to display this chat message

        Arguments
        - format: String.Format compatible format string
        """
        ...


    def getRecipients(self) -> set["Player"]:
        """
        Gets a set of recipients that this chat message will be displayed to

        Returns
        - All Players who will see this chat message
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
